# Income Gauge: Predicting-Economic-Disparities-Using-ML
This project leverages machine learning to predict income levels by providing a model embeded in a Streamlit framework that predicts whether an individual earns above or below a specified amount.

## Table of Contents
- [Business Understanding](#business-understanding)
    - [Hypothesis Testing](#hypothesis-testing)
- [Data Understanding](#data-understanding)
- [App Features](#app-features)
    - [Login Page](#1-login-page)
    - [Home Page](#2-home-page)
    - [Data Page](#3-data-page)
    - [Predict Page](#4-predict-page)
    - [History Page](#5-history-page)
    - [Dashboard Page](#6-dashboard-page)
- [Usage](#usage)
- [Contributing](#contributing)
- [Resources](#resources)
- [Author](#author)
- [Hyperlinks](#hyperlinks)

## **Business Understanding**
Income inequality, characterized by the uneven distribution of earnings across a population, is a growing challenge in developing nations. With the rapid advancement of AI and automation technologies, this disparity is projected to increase unless proactive measures are taken.

This project follows the CRISP-DM framework with the objective of developing a machine learning model that predicts whether an individual, based on specific characteristics, is likely to earn above or below a $50,000 threshold. The best performing models will then be deployed for practical use.

By implementing this solution, we aim to enhance the accuracy and reduce the cost of tracking key population metrics, such as income levels, between census periods. This will empower policymakers to make more informed decisions and take effective actions to mitigate income inequality globally.

### Hypothesis Testing
- **Null Hypothesis (Ho):** Level of education has no statistical significance influence on Income limit 
- **Alternate Hypothesis (Ha):** Level of education has statistical significance influence on Income limit

[Back to Table of Contents](#table-of-contents)

## **Data Understanding**
The dataset consists of various features that provide detailed information about individuals, ranging from demographic details to employment and migration history.<br>

`Key Features:`

<div style="display: flex; justify-content: space-between;">
<div style="width: 50%;">

- **ID**: Unique identifier for each individual.
- **age**: Age of the individual.
- **gender**: Gender of the individual.
- **education**: Level of education of the individual.
- **marital_status**: Marital status of the individual.
- **race**: Race of the individual.
- **is_hispanic**: Indicator for Hispanic ethnicity.
- **employment_commitment**: Employment status of the individual.
- **employment_stat**: Employment status of the individual.
- **wage_per_hour**: Hourly wage of the individual.
- **working_week_per_year**: Number of weeks worked per year.
- **industry_code**: Code representing the industry of employment.
- **industry_code_main**: Main industry code.
- **occupation_code**: Code representing the occupation.
- **total_employed**: Total number of individuals employed.
- **household_stat**: Household status.
</div>
<div style="width: 50%;">

- **household_summary**: Summary of household information.
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
</div>
</div>

[Back to Table of Contents](#table-of-contents)

## **App Features**
### 1. Login Page
- **Overview:** Serves as a login gateway for users to access the application after authentication.
- **Key Elements:**
    - Provides login credential for users   

<img src="assets\login_interface.JPG" alt="Home Page" width="850"/>

[Back to Table of Contents](#table-of-contents)

### 2. Home Page
- **Overview:** Introduces the application and its purpose.
- **Key Elements:**
    - Provides an overview of the application.
    - Includes background information about the developer.

<img src="assets\home_page.JPG" alt="Home Page" width="850"/>

[Back to Table of Contents](#table-of-contents)


### 3. Data Page
- **Overview:** Offers insights into the data used for predictions and individual's attributes required for accurate predictions.
- **Key Features:**
    - Hosts data used for app development and testing **(Data can be downloaded and used to test the app).**
    - Allows users to upload their own data for analysis.
    - Allows users to chunk data based on selected size and explore
    - Provides comprehensive information about the data.
    - Ensures seamless integration of uploaded data into the prediction process on the Predict Page.

<img src="assets\data_page1.JPG" alt="Data Page" width="850"/>
<img src="assets\data_page2.JPG" alt="Data Page" width="850"/>

[Back to Table of Contents](#table-of-contents)

### 4. Predict Page
- **Overview:** Enables income disparity predictions, showing both income level **(Above Limit or Below Limit)** and prediction probability.
- **Key Features:**
    - Allows individual's details to be entered for `single predictions`.
    - Allows predictions using previously uploaded data from the data page.
    - Utilizes the following models for predictions:
        1. **XGBoost Classifier:** Employed for both single and bulk predictions as the top-performing model.
        2. **Random Forest Classifier:** Used exclusively for single predictions.

<img src="assets\prediction_page1.JPG" alt="Predict Page" width="850"/>
<img src="assets\prediction_page2.JPG" alt="Predict Page" width="850"/>

[Back to Table of Contents](#table-of-contents)

### 5. History Page
- **Overview:** Provides a record of all predictions made by the user.
- **Key Features:**
    - Provides a detailed record of all user predictions for reference and analysis.
    - Individual predictions are added to the top of the history.
    - Bulk predictions replace existing history to facilitate dashboard analysis.
 
<img src="assets\history_page1.JPG" alt="History Page" width="850"/>
<img src="assets\history_page2.JPG" alt="History Page" width="850"/>

[Back to Table of Contents](#table-of-contents)

### 6. Dashboard Page
- **Overview:** Displays interactive visualizations for quick insights.
- **Key Features:**
    - **Exploratory Data Analysis (EDA) Dashboard:** Provides comprehensive visualizations and analyses of the data.
    - **Key Indicator Dashboard:** Showcases critical metrics through interactive visualizations.
    - **Dynamic Filtering and KPI Updates:** Users can filter data and update key performance indicators (KPIs) such as Percentage Count of Income Limit, Education level, and Industry.

<img src="assets\dashboard_page1.JPG" alt="Dashboard" width="850"/>
<img src="assets\dashboard_page2.JPG" alt="Dashboard" width="850"/>

[Back to Table of Contents](#table-of-contents)

## Usage
1. **Launch the Application:** Initiate the application using [Income Gaue app](https://incomepredictor-predicting-economic-vuqa.onrender.com)
2. **Select a Dataset:** Upload your data.
3. **Make Predictions:** Perform either single or bulk predictions.
4. **Review Prediction History:** Access and navigate through the prediction history.
5. **Explore Results:** Analyze the results and visualizations on the interactive dashboard.

[Back to Table of Contents](#table-of-contents)

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.<br>For major changes, please open an issue first to discuss what you would like to change.

[Back to Table of Contents](#table-of-contents)

## Resources
- [Get Started with Streamlit](https://docs.streamlit.io/get-started/tutorials/create-an-app): A comprehensive guide to building your first Streamlit application.
- [Streamlit API Reference](https://docs.streamlit.io/library/api-reference): Detailed documentation on Streamlit's API for customizing and extending your app.
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet): A quick reference guide for commonly used Streamlit commands and features.
- [Python for Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/): A resourceful book covering essential Python libraries like NumPy, Pandas, Matplotlib, and more, useful for data analysis and manipulation.
- [Machine Learning with Scikit-Learn](https://scikit-learn.org/stable/): Official documentation for Scikit-Learn, which is invaluable for implementing and understanding machine learning models.
- [Plotly Documentation](https://plotly.com/python/): Learn how to create interactive visualizations with Plotly, which can be integrated into your Streamlit app.
- [Deploying Streamlit Apps](https://docs.streamlit.io/streamlit-cloud/get-started): A guide on deploying your Streamlit application to the cloud, making it accessible to others.

[Back to Table of Contents](#table-of-contents)

## Author
- <img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='GitHub' height='20' style='filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(0deg) brightness(100%) contrast(100%); margin-right: 8px;'> [GitHub](https://github.com/edadso)
- <img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg' alt='LinkedIn' height='20' style='filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(0deg) brightness(100%) contrast(100%); margin-right: 8px;'> [LinkedIn](https://www.linkedin.com/in/emmanuel-dadson)
- <img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/medium.svg' alt='Medium' height='20' style='filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(0deg) brightness(100%) contrast(100%); margin-right: 8px;'> [Medium](https://medium.com/@emmanueldadson36)
- <img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/gmail.svg' alt='Email' height='20' style='filter: invert(100%) sepia(0%) saturate(0%) hue-rotate(0deg) brightness(100%) contrast(100%); margin-right: 8px;'> emmanueldadson36@gmail.com            

[Back to Table of Contents](#table-of-contents)

## Hyperlinks
- [Render Deployment](https://incomepredictor-predicting-economic-vuqa.onrender.com)
- [Streamlit Deployment](https://income-predictor-app.streamlit.app)

[Back to Table of Contents](#table-of-contents)


