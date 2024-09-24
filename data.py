import streamlit as st
import pandas as pd
import numpy as np
import time

def show_data():
    user_choice = st.sidebar.radio("### Select a page", options = ["Data Understanding", "Data Hub"], key = "option_selected")

    if user_choice == "Data Understanding":
        st.info("## 📚 Data Understanding")
        st.markdown(
                        """
                        The dataset consists of various features that provide detailed information about individuals,
                        ranging from demographic details to employment and migration history. The models were trained
                        on these features

                        #### Feature Description:
                        """
                        )

        # Create columns
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                - **ID**: Unique identifier for each individual.
                - **age**: Age of the individual.
                - **gender**: Gender of the individual.
                - **education**: Level of education of the individual.
                - **marital_status**: Marital status of the individual.
                - **race**: Race of the individual.
                - **is_hispanic**: Indicator for Hispanic ethnicity.
                - **employment_commitment**: Employment status of the individual.
                - **employment_stat**: Employment status of the individual **(0: Unemployed, 1: Employed, 2: Part-time)**
                - **wage_per_hour**: Hourly wage of the individual.
                - **working_week_per_year**: Number of weeks worked per year.
                - **industry_code**: Code representing the industry of employment.
                - **occupation_code**: Code representing the occupation.
                - **total_employed**: Total number of individuals employed.
                """
                )

        with col2:
            st.markdown(
                """
                - **vet_benefit**: Veteran benefits received.
                - **tax_status**: Tax status of the individual.
                - **gains**: Financial gains.
                - **losses**: Financial losses.
                - **stocks_status**: Status of stocks owned.
                - **citizenship**: Citizenship status.
                - **mig_year**: Year of migration.
                - **country_of_birth_own**: Country of birth of the individual.
                - **country_of_birth_father**: Country of birth of the individual’s father.
                - **country_of_birth_mother**: Country of birth of the individual’s mother.
                - **importance_of_record**: Importance of the record.
                - **income_above_limit**: Indicator for income above a certain limit.
                - **household_stat**: Household status.
                - **household_summary**: Summary of household information.
                """
                )
            
    if user_choice == "Data Hub":
        st.markdown("<h1 style='color: lightblue;'>📚 Data Hub</h1>", unsafe_allow_html = True)
        st.info("### *Welcome To Data Hub*")
        st.markdown("#### **Uploaded data will be available for prediction in the predict page**") 

        # Load csv data in chunks
        @st.cache_data
        def load_data_in_chunks(file_path, chunk_size, start_chunk):
            try:
                chunks = pd.read_csv(file_path, chunksize = chunk_size)
                for idx, chunk in enumerate(chunks):
                    if idx == start_chunk:
                        return chunk
            except Exception as e:
                st.error(f"Error loading data: {str(e)}")
            return None
        
        # Load excel data in chunks
        @st.cache_data
        def load_xlsx_in_chunks(file_path, chunk_size, start_chunk):
            try:
                chunks = pd.read_excel(file_path, chunksize=chunk_size)
                for idx, chunk in enumerate(chunks):
                    if idx == start_chunk:
                        return chunk
            except Exception as e:
                st.error(f"Error loading Excel data: {str(e)}")
            return None

        # Clean dataset
        def clean_columns(data_chunk):
            columns_to_drop = ["class", "education_institute", "unemployment_reason", "is_labor_union",
                            "occupation_code_main", "under_18_family", "veterans_admin_questionnaire",
                            "migration_code_change_in_msa", "migration_prev_sunbelt", 
                            "migration_code_move_within_reg", "migration_code_change_in_reg",
                            "residence_1_year_ago", "old_residence_reg", "old_residence_state"]

            data_chunk = data_chunk.drop(columns = columns_to_drop, axis=1)
            for col in data_chunk.select_dtypes(include = ["category", "object"]).columns:
                data_chunk[col] = data_chunk[col].str.strip()
            data_chunk.replace("?", np.nan, inplace = True)
            data_chunk["is_hispanic"] = data_chunk["is_hispanic"].replace("NA", "All other")
            return data_chunk

        # Data preview section
        with st.expander("## **Explore the dataset used for testing here**", expanded = False):

            st.sidebar.info("**Explore Test Data Here 👇**")          
            # Define chunk size
            chunk_size_1 = 20000
            # Allow user select page number to access chunked data
            page_number = st.sidebar.number_input("Select Page", min_value = 0, value = 0, step = 1, key = "page_num_1")
            data_chunk = load_data_in_chunks("data/Test.csv", chunk_size_1, page_number)
            
            if data_chunk is not None:
                st.write(f"Displaying page {page_number + 1} (Rows {page_number * chunk_size_1 + 1} to {(page_number + 1) * chunk_size_1})")
                data_chunk_1 = clean_columns(data_chunk)
                st.dataframe(data_chunk)

                if st.sidebar.button("View Stats", key = "data_statistics_1"):
                    st.write("#### Data Statistics")
                    st.write(data_chunk.describe())

                if st.sidebar.button("View Data Shape", key = "data_shape_1"):
                    st.write("#### Data Shape")
                    st.write(data_chunk.shape)

                if st.sidebar.button("Count Missing values", key = "missing_values_1"):
                    st.write("#### Missing Values")
                    null_count = data_chunk.isnull().sum().reset_index()
                    null_count.columns = ["Features", "Missing Value Counts"]
                    st.write(null_count)

                if st.sidebar.button("View Unique Values", key = "unique_values_1"):
                    st.write("#### Unique Values")
                    unique_count = data_chunk.nunique().reset_index()
                    unique_count.columns = ["Features", "Unique Counts"]
                    st.write(unique_count)
            else:
                st.write("No more data to display.")

        # Upload your dataset
        with st.expander("**Upload your dataset here**", expanded = False):
            upload_file = st.file_uploader(label = "Choose a file", type = ["csv", "xlsx"])

            if "data_loaded" not in st.session_state:
                st.session_state.data_loaded = False

            if upload_file is not None:
                st.sidebar.info("**Explore Uploaded Data Here 👇**")
                try:
                    if upload_file.name.endswith(".csv"):
                        file_size = upload_file.size / (1024 * 1024)  # Convert to MB
                        if file_size > 10:
                            st.warning("Large file detected! Loading in chunks.")
                            # Allow the user to choose the chunk size
                            chunk_size = st.sidebar.slider("Choose chunk size (rows per chunk)", 1000, 25000, 20000, key = "chunk_size_2")
                            page_number = st.sidebar.number_input("Select Page", min_value = 0, value = 0, step = 1, key = "page_num_2")
                            data_chunk = load_data_in_chunks(upload_file, chunk_size, page_number)

                            if data_chunk is not None:
                                st.write(f"Displaying page {page_number + 1} (Rows {page_number * chunk_size + 1} to {(page_number + 1) * chunk_size})")
                                data = clean_columns(data_chunk)
                                st.session_state["uploaded_data"] = data
                                st.dataframe(data)
                        else:
                            data = pd.read_csv(upload_file)
                            data = clean_columns(data)
                            st.session_state["uploaded_data"] = data
                            st.subheader("Data Preview")
                            st.dataframe(data.head())

                    elif upload_file.name.endswith(".xlsx"):
                        file_size = upload_file.size / (1024 * 1024)
                        if file_size > 10:
                            st.warning("Large file detected! Loading in chunks.")
                            # Allow the user to choose the chunk size
                            chunk_size = st.sidebar.slider("Choose chunk size (rows per chunk)", 1000, 25000, 20000, key = "chunk_size_3")
                            page_number = st.sidebar.number_input("Select Page", min_value = 0, value = 0, step = 1, key = "page_num_3")
                            data_chunk = load_xlsx_in_chunks(upload_file, chunk_size, page_number)

                            if data_chunk is not None:
                                st.write(f"Displaying page {page_number + 1} (Rows {page_number * chunk_size + 1} to {(page_number + 1) * chunk_size})")
                                data = clean_columns(data_chunk)
                                st.session_state["uploaded_data"] = data
                                st.dataframe(data)
                        else:
                            data = pd.read_excel(upload_file)
                            data = clean_columns(data)
                            st.session_state["uploaded_data"] = data
                            st.subheader("Data Preview")
                            st.dataframe(data.head())

                except Exception as e:
                    st.error(f"Error reading this file: {str(e)}")

                if not st.session_state.data_loaded:

                    # Display success message
                    success_msg = st.empty()
                    success_msg.success("Data uploaded successfully!")
                    # Display success message for 2 seconds
                    time.sleep(2)
                    # Clear success message
                    success_msg.empty()
                    st.session_state.data_loaded = True

                # Extra options for data exploration
                if st.sidebar.button("View Stats", key = "data_statistics_2"):
                    st.write("#### Data Statistics")
                    st.write(data.describe())

                if st.sidebar.button("View Data Shape", key = "data_shape_2"):
                    st.write("#### Data Shape")
                    st.write(data.shape)

                if st.sidebar.button("Count Missing values", key = "missing_values_2"):
                    st.write("#### Missing Values")
                    null_count = data.isnull().sum().reset_index()
                    null_count.columns = ["Features", "Missing Value Counts"]
                    st.write(null_count)

                if st.sidebar.button("View Unique Values", key = "unique_values_2"):
                    st.write("#### Unique Values")
                    unique_count = data.nunique().reset_index()
                    unique_count.columns = ["Features", "Unique Counts"]
                    st.write(unique_count)
            else:
                st.error("Please upload a CSV or XLSX file.")