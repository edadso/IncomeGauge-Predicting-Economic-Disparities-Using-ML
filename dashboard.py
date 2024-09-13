import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import os


def show_dashboard():
    # Radio widget to select dashboard choice
    dashboard_choice = st.sidebar.radio("Select Dashboard", ["EDA Dashboard", "KPI Dashboard"])

    # Load history data
    @st.cache_data
    def load_dashboard_data():
        if os.path.exists("data/uploaded_data_history.csv"):
            data = pd.read_csv("data/uploaded_data_history.csv")
        else:
            st.error("## No Data Available")
        return data
        
    df = load_dashboard_data()

    # Use the loaded data for dashboard based on user’s selected dashboard
    if df is not None and not df.empty:
    
        if dashboard_choice == "EDA Dashboard":

            # Align dashboad name to the centre
            left, middle, right = st.columns([1, 5, 1])
            with middle:
                # Sidebar for dashboard selection
                st.markdown("<h1 style='color: lightblue;'> 🔍 Exploratory Data Analysis</h1>", unsafe_allow_html=True)

            # Preview data frame
            st.dataframe(df.head())

            # Create 3 columns for layout
            col1, col2, col3 = st.columns(3)
            with col1:
                # Box plot for age, working_week_per_year, etc.
                fig1 = px.box(df[["age", "working_week_per_year", "industry_code", "occupation_code", "total_employed", "mig_year"]],
                            title = "Box plots of Key Features", template = "plotly_dark", color_discrete_sequence=px.colors.qualitative.Bold)
                st.plotly_chart(fig1)

            with col2:
                # Box plot for other important features
                fig2 = px.box(df[["losses", "importance_of_record", "gains", "wage_per_hour"]],
                                title = "Box plots of Economic Factors", color_discrete_sequence=px.colors.qualitative.Bold)
                st.plotly_chart(fig2)

            with col3:
                # Box plot for stocks_status
                fig3 = px.box(df[["stocks_status"]], title = "Box plot of Stock Status",
                            color_discrete_sequence=px.colors.qualitative.Bold)
                st.plotly_chart(fig3)

            # Align heatmap to the centre
            left, middle, right = st.columns([1, 10, 1])
            with middle:
                # Global Correlation Heatmap (applicable to both dashboards)
                filter_df = df[["age", "employment_stat", "wage_per_hour", "working_week_per_year", "industry_code", "occupation_code",
                                "total_employed", "vet_benefit", "gains", "losses", "stocks_status", "mig_year", "importance_of_record", "income_above_limit"]]

                # Dropping NaN values
                filter_df.dropna(inplace = True)

                # Mapping the target variable for correlation
                filter_df["income_above_limit"] = filter_df["income_above_limit"].map({"Above limit": 1, "Below limit": 0})

                # Compute the correlation matrix
                corr = filter_df.corr()

                # Heatmap Plot using Plotly
                heatmap_fig = go.Figure(data=go.Heatmap(z = corr.values,
                                                        x = corr.columns,
                                                        y = corr.columns,
                                                        colorscale = "Viridis"))

                heatmap_fig.update_layout(title = "Correlation Heatmap", width = 800, height = 600)
                st.plotly_chart(heatmap_fig)


            # Create 3 columns for layout
            col1, col2, col3 = st.columns(3)
            with col1:
                # KPI Countplot 1: Gender vs Income
                fig4 = px.histogram(df, x = "gender", color = "income_above_limit", barmode = "group",
                                    title = "Income Distribution by Gender", color_discrete_sequence = ["green", "lightgreen"])
                st.plotly_chart(fig4)

            with col2:
                # KPI Countplot 2: Education vs Income
                fig5 = px.histogram(df, x = "education", color = "income_above_limit", barmode = "group",
                                    title = "Income Distribution by Education", color_discrete_sequence = ["green", "lightgreen"])
                st.plotly_chart(fig5)

            with col3:
                # KPI Countplot 3: Marital Status vs Income
                fig6 = px.histogram(df, x = "marital_status", color = "income_above_limit", barmode = "group",
                                    title = "Income Distribution by Marital Status", color_discrete_sequence = ["green", "lightgreen"])
                st.plotly_chart(fig6)


        elif dashboard_choice == "KPI Dashboard":
            # Align title of dashboard to the centre
            left, middle, right = st.columns([1, 5, 1])
            with middle:
                st.markdown("<h1 style='color: lightblue;'> 💡 Income Level Indicator Dashboard</h1>", unsafe_allow_html=True)

            # Sidebar widgets
            st.sidebar.header("Filter Options")

            # Age slider
            age = st.sidebar.slider("Age", 0, int(df["age"].max()), (0, int(df["age"].max())), key = "age")

            # Gender selectbox
            gender = st.sidebar.selectbox("Gender", options = ["Female", "Male"], key = "gender")

            # Tax status selectbox
            tax_status = st.sidebar.selectbox("Tax Status", options = [
                "Head of household", "Single", "Nonfiler", "Joint both 65+", "Joint both under 65", "Joint one under 65 & one 65+"], key = "tax_status")

            # Filter the data based on sidebar input
            filtered_df = df[(df["age"] >= age[0]) & (df["age"] <= age[1]) & 
                            (df["gender"] == gender) & 
                            (df["tax_status"] == tax_status)]

            # Check if the filtered DataFrame is empty
            if filtered_df.empty:
                st.warning("No data available for the selected filters. Please adjust your filters.")
            else:
                # Metrics
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Above Limit Count", filtered_df[filtered_df["income_above_limit"] == "Above limit"].shape[0])

                with col2:
                    st.metric("Below Limit Count", filtered_df[filtered_df["income_above_limit"] == "Below limit"].shape[0])

                with col3:
                    st.metric("Male Count", filtered_df[filtered_df["gender"] == "Male"].shape[0])

                with col4:
                    st.metric("Female Count", filtered_df[filtered_df["gender"] == "Female"].shape[0])

                # Split layout into two columns for visualizations
                left, right = st.columns(2)
                with left:
                    # Add Pie chart (Percentage of above and below limit from income_above_limit column)
                    income_counts = filtered_df["income_above_limit"].value_counts()
                    pie_fig = px.pie(values = income_counts, names = income_counts.index,
                                    title = "Income Above/Below Limit",
                                    color_discrete_sequence = ["blue", "lightblue"])
                    st.plotly_chart(pie_fig)

                    # Add horizontal chart for education
                    income_limit_proportion_by_education = (
                        filtered_df.groupby(by = ["education", "income_above_limit"])
                        .size().unstack().apply(lambda x: x / x.sum() * 100, axis = 1)
                        .sort_values(by = "Above limit", ascending = True)
                    )
                    # Plot horizontal bar chart
                    fig_bar = px.bar(income_limit_proportion_by_education, orientation = 'h', 
                                    title = "Proportion of Income Limit by Education",
                                    color_discrete_sequence = ["blue", "lightblue"])
                    st.plotly_chart(fig_bar)

                    
                with right:
                    # Plotly Express Choropleth for country of birth
                    fig_map = px.choropleth(
                        filtered_df, 
                        locations = "country_of_birth_own", 
                        locationmode = "country names",
                        color = "income_above_limit", 
                        hover_name = "country_of_birth_own", 
                        color_continuous_scale = px.colors.sequential.Plasma,
                        title = "Income Disparity by Country"
                    )
                    # Display the map in Streamlit
                    st.plotly_chart(fig_map)


                    # Add horizontal chart for industry
                    income_limit_proportion_by_industry = (
                        filtered_df.groupby(by = ["industry_code_main", "income_above_limit"])
                        .size().unstack().apply(lambda x: x / x.sum() * 100, axis = 1)
                        .sort_values(by = "Above limit", ascending = True)
                    )
                    # Plot horizontal bar chart for industry
                    fig_bar_industry = px.bar(income_limit_proportion_by_industry, orientation = "h", 
                                            title = "Proportion of Income Limit by Industry",
                                            color_discrete_sequence = ["blue", "lightblue"])
                    st.plotly_chart(fig_bar_industry)




                



