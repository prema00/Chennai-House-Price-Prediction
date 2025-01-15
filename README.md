# Cellphone Price Prediction

## Overview
This project analyzes a dataset of mobile phone features to explore their relationships with price categories. The goal is to identify patterns and build predictive models that classify mobile phones into different price ranges.

## Dataset
The dataset contains the following attributes:
- **battery_power**: Battery capacity in mAh.
- **blue**: Bluetooth support (1 = Yes, 0 = No).
- **clock_speed**: Processor speed in GHz.
- **dual_sim**: Dual SIM support (1 = Yes, 0 = No).
- **fc**: Front camera megapixels.
- **four_g**: 4G support (1 = Yes, 0 = No).
- **int_memory**: Internal memory in GB.
- **m_dep**: Mobile depth in cm.
- **mobile_wt**: Weight of the phone in grams.
- **n_cores**: Number of processor cores.
- **pc**: Primary camera megapixels.
- **px_height**: Pixel resolution height.
- **px_width**: Pixel resolution width.
- **ram**: RAM in MB.
- **sc_h**: Screen height in cm.
- **sc_w**: Screen width in cm.
- **talk_time**: Battery talk time in hours.
- **three_g**: 3G support (1 = Yes, 0 = No).
- **touch_screen**: Touchscreen support (1 = Yes, 0 = No).
- **wifi**: WiFi support (1 = Yes, 0 = No).
- **price_range**: Target variable (0 = Low, 1 = Medium, 2 = High, 3 = Very High).

## Objectives
1. Understand the relationships between mobile phone features and their impact on price range.
2. Visualize the data to uncover insights.
3. Build machine learning models for price range classification.

## Visualizations
The project includes several meaningful visualizations:
- Distribution of price ranges.
- Box plots for features like RAM and battery capacity.
- Scatter plots for screen resolution and talk time vs. battery power.
- Correlation heatmaps to identify significant relationships.
- Bar charts showing the impact of features like core count, dual SIM, and connectivity options.

## Tools and Libraries
- **Python**: Core programming language.
- **Pandas**: For data manipulation.
- **Matplotlib & Seaborn**: For data visualization.
- **Scikit-learn**: For machine learning and feature importance.

## Project Workflow
1. **Data Cleaning**: Ensure all features are properly formatted and handle missing values if any.
2. **Exploratory Data Analysis (EDA)**: Generate meaningful insights through visualizations.
3. **Feature Engineering**: Identify important features for prediction.
4. **Model Building**: Train models to classify phones into price categories.
5. **Evaluation**: Assess model performance using appropriate metrics.

## How to Use
1. Clone the repository:
   ```bash
   git clone <repository-link>
