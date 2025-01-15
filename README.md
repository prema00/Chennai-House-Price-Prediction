Chennai House Price Prediction

Overview

This project focuses on analyzing and predicting house prices in Chennai based on various features. The objective is to understand key factors influencing house prices and develop predictive models for accurate pricing.

Dataset

The dataset contains the following attributes:

area_type: Type of the area (e.g., Super Built-up Area, Built-up Area).

availability: Availability status of the property.

location: Location of the property.

size: Number of bedrooms (e.g., 2 BHK, 3 BHK).

society: Name of the society (if applicable).

total_sqft: Total square footage of the property.

bath: Number of bathrooms.

balcony: Number of balconies.

price: Price of the property (target variable).

Objectives

Explore the relationships between property features and their prices.

Visualize the distribution and trends in the data.

Build predictive models to estimate house prices based on given features.

Visualizations

The project includes the following visualizations:

Distribution of house prices.

Scatter plots for total square footage vs. price.

Box plots for price by area type and number of bedrooms.

Heatmap showing correlations between numerical features.

Bar charts for categorical variables like location and availability.

Tools and Libraries

Python: Core programming language.

Pandas: For data manipulation.

Matplotlib & Seaborn: For data visualization.

Scikit-learn: For machine learning and feature importance.

Project Workflow

Data Cleaning: Handle missing values, incorrect entries, and inconsistent formatting.

Exploratory Data Analysis (EDA): Generate insights and visualize patterns.

Feature Engineering: Create or transform features for better predictions.

Model Building: Train models to predict house prices.

Evaluation: Use metrics like RMSE, MAE, and R-squared to assess model performance.

How to Use

Clone the repository:

git clone <repository-link>

Install the required libraries:

pip install -r requirements.txt

Run the Jupyter Notebook:

jupyter notebook "Chennai House Price Prediction.ipynb"

Explore visualizations and predictions.

Future Work

Incorporate additional features like neighborhood amenities and market trends.

Experiment with advanced machine learning models for better accuracy.

Deploy the model as a web-based application for user interaction.

License

This project is licensed under the MIT License. See LICENSE for details.
