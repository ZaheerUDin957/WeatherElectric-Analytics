import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
import io  # Import io for StringIO

# Import custom CSS for styling
from styles import overall_css

# Function to check missing values
def check_missing_values(df):
    missing_values_count = df.isnull().sum()
    missing_values_percentage = 100 * missing_values_count / len(df)
    missing_values_df = pd.DataFrame({
        'Column': df.columns,
        'Missing Values': missing_values_count,
        'Percentage Missing': missing_values_percentage
    })
    missing_values_df.reset_index(drop=True, inplace=True)
    return missing_values_df

# Function to drop missing values
def drop_missing_values(df):
    df = df.dropna()
    return df

# Function to plot missing values heatmap
def plot_missing_values_heatmap(df):
    missing_values = df.isnull()
    plt.figure(figsize=(12, 8))
    sns.heatmap(missing_values, cbar=False, cmap='viridis', yticklabels=False)
    plt.title('Heatmap of Missing Values')
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    st.pyplot(plt)

# Function to visualize outliers using Plotly
def visualize_outliers(df, column_name):
    fig = px.box(
        df,
        y=column_name,
        points="all",
        notched=True,
        title=f'Outliers in {column_name}',
        labels={column_name: column_name},
        hover_data=["Hour"],  # Include Hour in hover data (assuming Date isn't part of data in this snippet)
        template="presentation",
        color_discrete_sequence=["#636EFA"]
    )
    fig.update_layout(
        title=dict(x=0.5, font=dict(size=24)),
        yaxis_title=dict(font=dict(size=18)),
        xaxis=dict(tickfont=dict(size=14)),
        yaxis=dict(tickfont=dict(size=14)),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    fig.update_traces(
        marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')),
        selector=dict(type='box')
    )
    st.plotly_chart(fig)

# Function to impute outliers with median
def impute_outliers_with_median(df):
    # Ensure numeric columns are used for calculation
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    Q1 = df[numeric_columns].quantile(0.25)
    Q3 = df[numeric_columns].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df_cleaned = df.copy()
    for col in numeric_columns:
        df_cleaned[col] = np.where((df_cleaned[col] < lower_bound[col]) | (df_cleaned[col] > upper_bound[col]), df_cleaned[col].median(), df_cleaned[col])
    return df_cleaned

# Function to standardize data using StandardScaler
def standardize_data(df, numeric_columns):
    scaler = StandardScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    return df

# Function to perform PCA and display explained variance ratio
def perform_pca(df, features):
    X = df[features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA()
    X_pca = pca.fit_transform(X_scaled)
    explained_variance_ratio = pca.explained_variance_ratio_
    return explained_variance_ratio

# Function for feature selection using RFE
def select_features_rfe(df, features, target):
    X = df[features]
    model = LinearRegression()
    rfe = RFE(model, n_features_to_select=5)
    X_rfe = rfe.fit_transform(X, target)
    selected_features = features[rfe.support_]
    return selected_features

def show():
    # Apply overall styles
    st.markdown(overall_css, unsafe_allow_html=True)

    
    # Heading: Data Preprocessing
    st.markdown("<h1 id='data-preprocessing'>Data Preprocessing</h1>", unsafe_allow_html=True)
    st.write("""
        This section deals with data preprocessing. Here you can clean and transform the data to prepare it for analysis and modeling.
    """)

    # Load Data
    df = pd.read_csv('electric load.csv')
    df = df.head(500)

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Data Inspection
    st.markdown("<h2 id='1-data-inspection'>1. Data Inspection</h2>", unsafe_allow_html=True)
    
    st.markdown("<h3 id='11-head-of-the-dataset'>1.1 Head of the Dataset</h3>", unsafe_allow_html=True)
    st.write("First 10 rows of the dataset:")
    st.dataframe(df.head(10))

    st.markdown("<h3 id='12-tail-of-the-dataset'>1.2 Tail of the Dataset</h3>", unsafe_allow_html=True)
    st.write("Last 10 rows of the dataset:")
    st.dataframe(df.tail(10))

    st.markdown("<h3 id='13-data-information'>1.3 Data Information</h3>", unsafe_allow_html=True)
    buffer = io.StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())

    st.markdown("<h3 id='14-summary-statistics'>1.4 Summary Statistics</h3>", unsafe_allow_html=True)
    st.dataframe(df.describe())

    st.markdown("<h3 id='15-data-shape'>1.5 Data Shape</h3>", unsafe_allow_html=True)
    st.write(df.shape)

    st.markdown("<h3 id='16-data-description'>1.6 Data Description</h3>", unsafe_allow_html=True)
    st.write("""
        - **Date**: The date of the recorded observation.
        - **Hour**: The specific hour of the day for the observation, in increments of 0.5 hours.
        - **DryBulb**: The dry bulb temperature, measured in degrees Celsius.
        - **DewPnt (Dew Point)**: The temperature at which air becomes saturated with moisture and dew can form, measured in degrees Celsius.
        - **WetBulb**: The wet bulb temperature, measured in degrees Celsius.
        - **Humidity**: The relative humidity, expressed as a percentage.
        - **ElecPrice (Electricity Price)**: The price of electricity at the given hour, measured in an unspecified currency.
        - **SYSLoad (System Load)**: The total electrical load on the system at the given hour, measured in megawatts (MW).
    """)

    st.markdown("<h3 id='17-data-correlation'>1.7 Data Correlation</h3>", unsafe_allow_html=True)
    st.write("Let's examine the correlation between different variables in the dataset.")
    numeric_df = df.select_dtypes(include=[np.number])
    st.dataframe(numeric_df.corr())

    # Data Cleaning
    st.markdown("<h2 id='2-data-cleaning'>2. Data Cleaning</h2>", unsafe_allow_html=True)

    st.markdown("<h3 id='21-handling-missing-data'>2.1 Handling Missing Data</h3>", unsafe_allow_html=True)
    
    st.markdown("<h4 id='211-missing-value-report'>2.1.1 Missing Value Report</h4>", unsafe_allow_html=True)
    missing_values_report = check_missing_values(df)
    st.dataframe(missing_values_report)

    st.markdown("<h4 id='212-missing-values-heatmap'>2.1.2 Missing Values Heatmap</h4>", unsafe_allow_html=True)
    plot_missing_values_heatmap(df)

    st.markdown("<h4 id='213-drop-missing-values-and-display-report'>2.1.3 Drop Missing Values and Display Report</h4>", unsafe_allow_html=True)
    df = drop_missing_values(df)
    st.write("DataFrame after dropping rows with missing values:")
    missing_values_report = check_missing_values(df)
    st.dataframe(missing_values_report)

    st.markdown("<h3 id='22-duplicate-handling'>2.2 Duplicate Handling</h3>", unsafe_allow_html=True)
    
    # Count duplicate rows
    duplicate_count = df.duplicated().sum()
    st.write(f"Number of duplicate rows: {duplicate_count}")

    # Remove duplicates if any
    if duplicate_count > 0:
        df = df.drop_duplicates()
        st.write("Duplicates removed.")
    else:
        st.write("No duplicates found.")

    # Display count of duplicates and data shape after cleaning
    duplicate_count_after = df.duplicated().sum()
    st.write(f"Number of duplicate rows after cleaning: {duplicate_count_after}")
    st.write(f"Data shape after cleaning: {df.shape}")

    # Outliers Handling
    st.markdown("<h2 id='23-outliers-handling'>2.3 Outliers Handling</h2>", unsafe_allow_html=True)

    st.markdown("<h3 id='231-data-before-outlier-handling'>2.3.1 Data Before Outlier Handling</h3>", unsafe_allow_html=True)
    st.write("Visualizing outliers using box plots:")
    visualize_outliers(df, 'Hour')
    visualize_outliers(df, 'DryBulb')
    visualize_outliers(df, 'DewPnt')
    visualize_outliers(df, 'WetBulb')
    visualize_outliers(df, 'Humidity')
    visualize_outliers(df, 'ElecPrice')
    visualize_outliers(df, 'SYSLoad')

    st.markdown("<h3 id='232-impute-outliers-with-median'>2.3.2 Impute Outliers with Median</h3>", unsafe_allow_html=True)
    df = impute_outliers_with_median(df)
    df = impute_outliers_with_median(df)
    df = impute_outliers_with_median(df)
    st.write("Data after imputing outliers with median values:")

    st.markdown("<h3 id='233-data-after-outlier-handling'>2.3.3 Data After Outlier Handling</h3>", unsafe_allow_html=True)
    st.write("Visualizing outliers after handling:")
    visualize_outliers(df, 'Hour')
    visualize_outliers(df, 'DryBulb')
    visualize_outliers(df, 'DewPnt')
    visualize_outliers(df, 'WetBulb')
    visualize_outliers(df, 'Humidity')
    visualize_outliers(df, 'ElecPrice')
    visualize_outliers(df, 'SYSLoad')

    # Standardize Data
    st.markdown("<h2 id='3-data-standardization'>3. Data Standardization</h2>", unsafe_allow_html=True)
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df = standardize_data(df, numeric_columns)
    st.write("Data after standardization:")
    st.dataframe(df.head(10))

    # Dimensionality Reduction
    st.markdown("<h2 id='4-dimensionality-reduction-using-pca'>4. Dimensionality Reduction using PCA</h2>", unsafe_allow_html=True)
    explained_variance_ratio = perform_pca(df, numeric_columns)
    st.write("Explained variance ratio of the principal components:")
    st.bar_chart(explained_variance_ratio)

    # Feature Selection
    st.markdown("<h2 id='5-feature-selection'>5. Feature Selection</h2>", unsafe_allow_html=True)
    selected_features = select_features_rfe(df, numeric_columns, df['ElecPrice'])
    st.write("Selected features using RFE:")
    st.write(selected_features)
    columns_to_drop = ['sysload(D-1)', 'sysload(W-1)']
    df.drop(columns=columns_to_drop, inplace=True)
    # Save the cleaned dataframe
    df_cleaned = df.copy()
    # Provide download link
    csv = df_cleaned.to_csv(index=False).encode('utf-8')
    st.download_button("Download data as CSV", data=csv, file_name='df_cleaned.csv', mime='text/csv')
    df.head()



