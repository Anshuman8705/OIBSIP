Task 3 — Car Price Prediction with Machine Learning

AICTE Oasis Infobyte Internship (OIBSIP)

📌 Overview

This project is completed as Task 3 under the AICTE Oasis Infobyte Internship Program (OIBSIP).
The main objective is to build a Machine Learning model that predicts the selling price of a used car based on its features.

Car prices depend on several factors including:

Current ex-showroom price

Fuel type (Petrol/Diesel/CNG)

Transmission type (Manual/Automatic)

Selling type (Dealer/Individual)

Car age

Kilometers driven

Previous owner history

Using these attributes, a regression model was developed to accurately estimate a car's selling price.

📂 Dataset Description

The dataset contains the following columns:

| Column Name       | Description                      |
| ----------------- | -------------------------------- |
| **Car_Name**      | Name/model of the car            |
| **Year**          | Year of purchase                 |
| **Selling_Price** | Target variable (price in lakhs) |
| **Present_Price** | Current ex-showroom price        |
| **Driven_kms**    | Kilometers driven                |
| **Fuel_Type**     | Petrol / Diesel / CNG            |
| **Selling_type**  | Dealer / Individual              |
| **Transmission**  | Manual / Automatic               |
| **Owner**         | Number of previous owners        |

Target Variable:
Selling_Price

✔ Features Used (after feature engineering):

Present_Price

Driven_kms

Fuel_Type

Selling_type

Transmission

Owner

Car_Age (created from Year)

🛠️ Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Google Colab

🧹 Data Preprocessing Performed

Loaded dataset using Pandas

Checked for missing and inconsistent data

Cleaned column names and values

Converted Year → Car_Age

Dropped irrelevant columns like Car_Name

Encoded categorical features (One-Hot Encoding)

Performed Train-Test Split

Feature engineering to improve model accuracy

🤖 Model Used
RandomForestRegressor

This model was chosen because it:

Handles non-linear relationships

Works well on small-to-medium datasets

Produces high accuracy

Is less prone to overfitting compared to decision trees

The complete pipeline included:

Preprocessing (OneHotEncoding + numerical passthrough)

Random Forest Regressor

📊 Model Evaluation

The model was evaluated using:

MAE (Mean Absolute Error)

MSE (Mean Squared Error)

R² Score

A scatter plot of Actual vs Predicted Selling Prices was also used to visualize accuracy and understand model performance.

Predicting Price of a New Car

The model can take the following inputs:

Present Price

Driven Kilometers

Fuel Type

Transmission Type

Number of Owners

Car Age

Example Output:
Predicted Selling Price (in lakhs): 4.67
This shows how the system can estimate the market value of a used car based on its attributes.


📈 Project Flow Summary

Import Libraries

Load Dataset

Clean & Analyze Data

Feature Engineering → Car_Age

Encode Categorical Columns

Train-Test Split

Build ML Pipeline

Train Random Forest Model

Evaluate Model Performance

Predict Selling Price for New Car Data

Visualize results

📝 Conclusion

This project demonstrates how Machine Learning can solve real-world regression problems such as estimating used car prices.

Key Learnings:

Feature engineering

Handling mixed-type data

Building ML pipelines

Regression modeling with Random Forest

Model evaluation techniques

Making predictions from trained models

This task significantly improved my understanding of practical ML workflows and data preprocessing techniques.

📁 Files Included

Car_Price_Prediction.ipynb — Google Colab notebook

README.md — Project documentation

🙌 Submitted Under

AICTE × Oasis Infobyte Internship Program (OIBSIP)
Task 3 — Car Price Prediction with Machine Learning
