import streamlit as st
from styles import overall_css

def show():
    st.markdown(overall_css, unsafe_allow_html=True)

    # Table of Contents in the sidebar
    st.sidebar.title("Table of Contents")
    st.sidebar.markdown("""
    <ul>
        <li><a href="#1-overview">1. Overview</a></li>
        <li><a href="#2-motivation">2. Motivation</a></li>
        <li><a href="#3-success-metrics">3. Success Metrics</a></li>
        <li>
            <a href="#4-requirements-and-constraints">4. Requirements and Constraints</a>
            <ul>
                <li><a href="#4-1-functional-requirements">4.1 Functional Requirements</a></li>
                <li><a href="#4-2-non-functional-requirements">4.2 Non-functional Requirements</a></li>
                <li><a href="#4-3-constraints">4.3 Constraints</a></li>
                <li><a href="#4-4-out-of-scope">4.4 Out of Scope</a></li>
            </ul>
        </li>
        <li>
            <a href="#5-methodology">5. Methodology</a>
            <ul>
                <li><a href="#5-1-problem-statement">5.1 Problem Statement</a></li>
                <li><a href="#5-2-data">5.2 Data</a></li>
                <li>
                    <a href="#5-3-techniques">5.3 Techniques</a>
                    <ul>
                        <li><a href="#5-3-1-data-preprocessing-and-cleaning">5.3.1 Data Preprocessing and Cleaning</a></li>
                        <li><a href="#5-3-2-feature-engineering-and-selection">5.3.2 Feature Engineering and Selection</a></li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><a href="#6-exploratory-data-analysis-eda">6. Exploratory Data Analysis (EDA)</a></li>
        <li><a href="#7-conclusion">7. Conclusion</a></li>
    </ul>
    """, unsafe_allow_html=True)

    st.header("1. Overview", anchor="1-overview")
    st.write("""
        The objective of this project is to analyze a dataset containing various weather-related variables and electricity prices. 
        By exploring the relationships and trends within this dataset, we aim to gain insights that can inform decision-making processes 
        in the energy sector, potentially leading to better forecasting models and optimized energy usage.
    """)

    st.header("2. Motivation", anchor="2-motivation")
    st.write("""
        The motivation for this project stems from the growing need to understand how environmental factors impact electricity prices. 
        Accurate forecasting of electricity prices can help in better resource management, reduce costs, and improve the efficiency of energy consumption. 
        This analysis can be particularly beneficial for energy providers, policymakers, and consumers.
    """)

    st.header("3. Success Metrics", anchor="3-success-metrics")
    st.write("""
        The success of this project will be measured by:
        - The accuracy of any predictive models developed (e.g., RMSE, MAE).
        - The ability to uncover significant relationships between weather variables and electricity prices.
        - The clarity and usefulness of insights generated through exploratory data analysis (EDA).
        - The effectiveness of data preprocessing and feature engineering techniques applied.
    """)

    st.header("4. Requirements and Constraints", anchor="4-requirements-and-constraints")
    st.subheader("4.1 Functional Requirements", anchor="4-1-functional-requirements")
    st.write("""
        - Data collection and preprocessing.
        - Exploratory Data Analysis (EDA).
        - Feature engineering and selection.
        - Development of predictive models.
        - Validation and testing of models.
        - Documentation and reporting of findings.
    """)

    st.subheader("4.2 Non-functional Requirements", anchor="4-2-non-functional-requirements")
    st.write("""
        - Maintain data integrity and confidentiality.
        - Ensure computational efficiency and scalability.
        - Provide clear and interpretable results.
    """)

    st.subheader("4.3 Constraints", anchor="4-3-constraints")
    st.write("""
        - Availability and quality of data.
        - Computational resources and time constraints.
        - Potential missing or inconsistent data.
    """)

    st.subheader("4.4 Out of Scope", anchor="4-4-out-of-scope")
    st.write("""
        - Real-time data processing and predictions.
        - Integration with external systems or live databases.
        - Development of a user interface for the end-users.
    """)

    st.header("5. Methodology", anchor="5-methodology")
    st.subheader("5.1 Problem Statement", anchor="5-1-problem-statement")
    st.write("""
        To analyze and model the relationship between weather variables (DryBulb, DewPnt, WetBulb, Humidity) and electricity prices (ElecPrice) 
        to uncover significant trends and develop predictive models for electricity prices.
    """)

    st.subheader("5.2 Data", anchor="5-2-data")
    st.write("""
        The dataset contains the following columns:
        - DryBulb: Dry Bulb Temperature.
        - DewPnt: Dew Point Temperature.
        - WetBulb: Wet Bulb Temperature.
        - Humidity: Relative Humidity.
        - ElecPrice: Electricity Price.
    """)

    st.subheader("5.3 Techniques", anchor="5-3-techniques")
    st.write("""
        ### 5.3.1 Data Preprocessing and Cleaning
        - Handle missing values (e.g., imputation or removal).
        - Correct any inconsistencies or anomalies in the data.
        - Normalize or standardize variables if necessary.

        ### 5.3.2 Feature Engineering and Selection
        - Create new features based on domain knowledge (e.g., temperature differences).
        - Select the most relevant features using statistical methods or machine learning algorithms.
    """)

    st.header("6. Exploratory Data Analysis (EDA)", anchor="6-exploratory-data-analysis-eda")
    st.write("""
        Conduct a thorough EDA to understand the data distribution, identify patterns, and uncover relationships between variables. This includes:
        - Visualizing the distribution of each variable.
        - Exploring correlations between weather variables and electricity prices.
        - Identifying any seasonal trends or patterns.
        - Checking for outliers and their potential impact.
    """)

    st.header("7. Conclusion", anchor="7-conclusion")
    st.write("""
        Summarize the key findings from the EDA and any predictive models developed. Discuss the implications of these findings for energy management and forecasting. 
        Highlight any limitations encountered during the project and suggest areas for future research or improvement.
    """)
