import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

from styles import overall_css

df = pd.read_csv('df_cleaned.csv')

def show():
    st.markdown(overall_css, unsafe_allow_html=True)

    st.markdown("<h1>Exploratory Data Analysis (EDA)</h1>", unsafe_allow_html=True)
    st.write("""
        In this section, you can explore the data through various visualizations and statistical analysis to uncover patterns and insights.
    """)

    # Preliminary Analysis
    st.markdown("<h2>1. Preliminary Analysis</h2>", unsafe_allow_html=True)

    # 1.1 Correlation
    st.markdown("<h3>1.1 Correlation</h3>", unsafe_allow_html=True)
    st.write("What are the strengths and directions of correlations between key variables (DryBulb, DewPnt, WetBulb, Humidity, ElecPrice, SYSLoad), and are there significant positive or negative correlations indicating potential relationships between these variables?")
    plot_correlation_heatmaps(df)
    st.write("Correlation heatmaps provide a clear view of how variables relate to each other. High positive or negative correlations suggest potential dependencies.")

    # 1.2 Outlier Detection
    st.markdown("<h3>1.2 Outlier Detection</h3>", unsafe_allow_html=True)
    st.write("Which variables (DryBulb, DewPnt, WetBulb, Humidity, ElecPrice, SYSLoad) exhibit outliers, and how do these outliers impact the overall distribution and interpretation of the data?")
    plot_outlier_violin_plots(df)
    st.write("Violin plots highlight outlier ranges and their impact on data distribution, aiding in outlier identification and understanding.")

    # 1.3 General Trends
    st.markdown("<h2>1.3 General Trends</h2>", unsafe_allow_html=True)

    # 1.3.1 Distribution of Data
    st.markdown("<h3>1.3.1 Distribution of Data</h3>", unsafe_allow_html=True)
    st.write("How do the distributions of key variables (Hour, DryBulb, DewPnt, WetBulb, Humidity, ElecPrice, SYSLoad) look across the dataset, and are there noticeable patterns or clusters?")
    plot_histograms(df)
    st.write("Histograms show variable distributions, revealing clusters or patterns that may indicate data characteristics or anomalies.")

    # 1.3.2 Time Series Analysis
    st.markdown("<h3>1.3.2 Time Series Analysis</h3>", unsafe_allow_html=True)
    st.markdown("<h3>How do variables (DryBulb, DewPnt, WetBulb, Humidity, ElecPrice, SYSLoad) fluctuate over time, and are there seasonal trends or cyclical patterns?</h3>", unsafe_allow_html=True)
    plot_time_series_analysis(df)
    st.markdown("<h3>Time series plots visualize variable changes over time, highlighting trends and seasonal patterns relevant for forecasting and decision-making.</h3>", unsafe_allow_html=True)

def plot_correlation_heatmaps(df):
    numeric_df = df.select_dtypes(include=[np.number])
    pearson_corr = numeric_df.corr(method='pearson')
    spearman_corr = numeric_df.corr(method='spearman')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    im1 = ax1.imshow(pearson_corr, cmap='RdBu', vmin=-1, vmax=1)
    ax1.set_title('Pearson Correlation Heatmap', fontsize=16)
    ax1.set_xticks(np.arange(len(pearson_corr)))
    ax1.set_yticks(np.arange(len(pearson_corr)))
    ax1.set_xticklabels(pearson_corr.columns, rotation=45, ha="right")
    ax1.set_yticklabels(pearson_corr.index)
    plt.colorbar(im1, ax=ax1, format='%.2f')

    for i in range(len(pearson_corr)):
        for j in range(len(pearson_corr.columns)):
            ax1.text(j, i, f'{pearson_corr.iloc[i, j]:.2f}', ha="center", va="center", color="black")

    im2 = ax2.imshow(spearman_corr, cmap='RdBu', vmin=-1, vmax=1)
    ax2.set_title('Spearman Correlation Heatmap', fontsize=16)
    ax2.set_xticks(np.arange(len(spearman_corr)))
    ax2.set_yticks(np.arange(len(spearman_corr)))
    ax2.set_xticklabels(spearman_corr.columns, rotation=45, ha="right")
    ax2.set_yticklabels(spearman_corr.index)
    plt.colorbar(im2, ax=ax2, format='%.2f')

    plt.tight_layout()
    st.pyplot(fig)

def create_violin_plot(df, column):
    fig = px.violin(df, y=column, box=True, points='all')
    fig.update_layout(
        title={'text': f'Violin Plot for {column}', 'font': {'family': 'Times New Roman', 'size': 16, 'color': 'black', 'weight': 'bold'}, 'x': 0.5, 'xanchor': 'center'},
        xaxis_title={'text': 'Values', 'font': {'family': 'Times New Roman', 'size': 16, 'color': 'black', 'weight': 'bold'}},
        yaxis_title={'text': column, 'font': {'family': 'Times New Roman', 'size': 16, 'color': 'black', 'weight': 'bold'}},
        yaxis_tickfont={'family': 'Times New Roman', 'size': 16, 'color': 'black', 'weight': 'bold'},
        xaxis_tickfont={'family': 'Times New Roman', 'size': 16, 'color': 'black', 'weight': 'bold'},
        yaxis_zeroline=False
    )
    st.plotly_chart(fig)

def plot_outlier_violin_plots(df):
    for col in ['DryBulb', 'DewPnt', 'WetBulb', 'Humidity', 'ElecPrice', 'SYSLoad']:
        create_violin_plot(df, col)

def plot_histograms(df):
    for col in ['DryBulb', 'DewPnt', 'WetBulb', 'Humidity', 'ElecPrice', 'SYSLoad']:
        fig = px.histogram(df, x=col, title=f'Histogram of {col}', labels={'x': col, 'y': 'Frequency'})
        fig.update_layout(
            title_font_family='Arial',
            title_font_size=16,
            xaxis_title_font_family='Arial',
            xaxis_title_font_size=16,
            yaxis_title_font_family='Arial',
            yaxis_title_font_size=16,
            xaxis_tickfont_family='Arial',
            xaxis_tickfont_size=14,
            yaxis_tickfont_family='Arial',
            yaxis_tickfont_size=14,
            showlegend=False
        )
        st.plotly_chart(fig)

bright_colors = ['#FF1493', '#00FFFF', '#FF4500', '#7FFF00', '#9932CC', '#00CED1', '#FFD700']

# Ensure to create a DateTime column by combining Date and Hour
df['DateTime'] = pd.to_datetime(df['Date']) + pd.to_timedelta(df['Hour'], unit='H')

def plot_time_series(df, column, color, title):
    fig = px.line(df, x='DateTime', y=column, animation_frame='Hour', animation_group='DateTime', range_x=[df['DateTime'].min(), df['DateTime'].max()], range_y=[df[column].min(), df[column].max()], title=title)
    
    for frame in fig.frames:
        frame.data[0].line.color = color
    
    fig.update_traces(marker=dict(size=10))
    fig.update_layout(
        title_font_family='Times New Roman',
        title_font_size=16,
        title=dict(font=dict(family="Times New Roman", size=16, color="black")),
        xaxis_title=dict(font=dict(family="Times New Roman", size=16, color="black")),
        yaxis_title=dict(font=dict(family="Times New Roman", size=16, color="black")),
        xaxis_tickfont=dict(family="Times New Roman", size=14, color="black"),
        yaxis_tickfont=dict(family="Times New Roman", size=14, color="black")
    )
    st.plotly_chart(fig)

def plot_time_series_analysis(df):
    plot_time_series(df, 'DryBulb', bright_colors[0], 'Time Forecasting for DryBulb')
    plot_time_series(df, 'DewPnt', bright_colors[1], 'Time Forecasting for DewPnt')
    plot_time_series(df, 'WetBulb', bright_colors[2], 'Time Forecasting for WetBulb')
    plot_time_series(df, 'Humidity', bright_colors[3], 'Time Forecasting for Humidity')
    plot_time_series(df, 'ElecPrice', bright_colors[4], 'Time Forecasting for ElecPrice')
    plot_time_series(df, 'SYSLoad', bright_colors[5], 'Time Forecasting for SYSLoad')



if __name__ == '__main__':
    show()
