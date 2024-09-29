# PowerCo Data Analysis

## Overview
This repository contains the analysis of customer and pricing data for PowerCo, aimed at understanding customer behavior and identifying factors influencing churn. The analysis was conducted using Python in a Jupyter notebook, following a structured framework to explore the datasets provided by the client.

## Datasets
The analysis utilizes three datasets provided by PowerCo:

1. **Historical Customer Data**: Contains information about customer usage, sign-up dates, forecasted usage, and other relevant metrics.
2. **Historical Pricing Data**: Includes variable and fixed pricing data for energy consumption.
3. **Churn Indicator**: Indicates whether each customer has churned or not.

## Analysis Objectives
The primary objectives of the analysis were to:
- Determine the data types of each column in the datasets.
- Generate descriptive statistics to summarize the datasets.
- Visualize the distributions of key columns to understand customer behavior and pricing trends.

## Analysis Steps
The analysis was performed using the following steps:

1. **Data Loading**: The datasets were loaded into pandas DataFrames for analysis.
2. **Data Types Inspection**: The data types of each column were examined to understand the nature of the data.
3. **Descriptive Statistics**: Summary statistics were generated for each dataset to provide insights into the data distribution.
4. **Missing Values Check**: The presence of missing values was assessed to determine data quality.
5. **Distribution Visualization**: Histograms and density plots were created to visualize the distribution of key numeric columns.
6. **Churn Analysis**: The churn rates were analyzed in relation to customer characteristics and pricing data.
7. **Correlation Analysis**: A correlation matrix was computed to identify relationships between numeric features.

## Key Findings
- The distribution of electricity consumption showed a right skew, indicating that while most customers have low consumption, a few customers consume significantly more energy.
- Higher electricity consumption was correlated with increased churn rates, suggesting that high-usage customers may be more likely to switch providers.
- Churn rates varied by sales channel, indicating that targeted retention strategies may be beneficial for specific channels.
- Price trends over time revealed fluctuations in both off-peak and peak variable prices, which could impact customer satisfaction and retention.

## Visualization Examples
The following visualizations were created during the analysis:
- Histograms of electricity consumption and forecasted usage.
- Count plots showing churn rates by sales channel.
- Correlation heatmaps to visualize relationships between numeric features.

## Conclusion
This analysis provides valuable insights into customer behavior and pricing trends for PowerCo. The findings suggest that targeted strategies based on customer consumption patterns and sales channels could help reduce churn and improve customer retention.

## Usage
To run the analysis, clone this repository and open the Jupyter notebook provided. Ensure that you have the necessary libraries installed, including `pandas`, `numpy`, `matplotlib`, and `seaborn`.
