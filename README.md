# Used-car-price-prediction

## Overview
This project predicts the price of a used car using factors such as mileage, year, accident history, fuel type. Goal : help buyers and sellers estimate fair price.
## Dataset
* Source: [Kaggle - used] (https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset?resource=download)
* Size: 4009 rows, 10 features
* Key Features:
  * Mileage
  * Year
  * Accident history
  * Car brand
## Data cleaning
* Handle missing values, change yes/no into binary values
* Remove outliers in price, unnecessary columns
* Group mileage in bins, exterior color
* Converted string columns
* Create columns such as age of car, price/mile for better understanding

## Exploatory Data Analysis (EDA)
* Histogram of prices, car brands, mileage vs price
* Scatterplot of mileage vs price, age vs price
* Countplot of car brands
* Boxplots for accident history, clean title, fuel type, exterior color
* Barplot of price by maker
* Heatmap of feature correlations

## Predictive Modeling
Five models trained and evaluated :
* Linear Regression
* Ridge Regression
* Lasso Regression
* Random Forest
* Gradient Boosting
### Evaluation Metrics
* R^2 (Coefficient of Determination)
* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
### Best Model
* Gradient Boosting resulted in highest R^2 and lowest MAE/RMSE which makes it the most accurate model for car price prediction

## Results
* Mileage, car age, accident history and clean title are the most significant factors that affected car prices.
* Gradient Boosting dominated other models in all evaluation matrics
* Future improvements : feature engineering and considering the initial price of sale of the car.

## Tools
* Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)
* Jupyter Notebook
* Github

## Author
Hayden Chang
* Purdue University - Math/Statistics Major, CS & Management Minors
* Pursuing Data Science & Machine Learning

