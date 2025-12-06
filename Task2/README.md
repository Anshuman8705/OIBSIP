🌟 Task 2 — Unemployment Analysis with Python
AICTE Oasis Infobyte Internship (OIBSIP)

📌 Overview

This project is completed as Task 2 of my AICTE Oasis Infobyte Data Science Internship (OIBSIP).
The objective of this task is to analyze unemployment trends in India during the COVID-19 period using Python.
The dataset includes unemployment rates across states, regions, rural/urban classifications, and multiple time periods—making it ideal for real-world exploratory data analysis and visualization.


📂 Dataset Description


The dataset contains the following fields:

Region – Name of the Indian state/region

Date – Record-collection date

Frequency – Monthly/Annual

Estimated Unemployment Rate (%) – Estimated unemployment percentage

Estimated Employed – Number of employed individuals

Estimated Labour Participation Rate (%) – Participation of working population

Area – Classification as Rural or Urban


Dataset Source:
✔ Kaggle – Unemployment in India (COVID-19 Period)
Dataset Code: gokulrajkmv/unemployment-in-india

🛠️ Technologies & Libraries Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Google Colab

KaggleHub (for dataset import)


📊 Tasks Performed


1️⃣ Data Loading

Downloaded dataset using kagglehub

Loaded CSV with Pandas

Displayed initial rows & verified dataset structure

Checked column names & data types


2️⃣ Data Cleaning & Preprocessing

Renamed columns for easier use

Converted Date column to datetime format

Removed missing/unwanted values

Standardized dataset for further analysis

3️⃣ Exploratory Data Analysis (EDA)

✔ Region-wise Unemployment (Bar Plot)

Identified states with the highest unemployment during COVID.

✔ Unemployment Trend Over Time (Line Plot)

Analyzed how unemployment fluctuated month-to-month.

✔ Multi-Region Trend Comparison

Visualized unemployment curves for each region.

✔ Correlation Heatmap

Explored relationships between:

Unemployment Rate

Labour Participation Rate

Number of Employed


4️⃣ Additional Analysis


Computed average unemployment for each state

Identified highest-impact COVID lockdown months

Compared Rural vs Urban unemployment

Highlighted states with major economic impact


⭐ Key Insights


Sharp spike in unemployment during April–May 2020 (strict lockdown period)

States like Puducherry, Jharkhand, Bihar, Rajasthan showed highest unemployment

Labour Participation Rate dropped significantly in the early COVID months

Urban unemployment was initially higher, but both rural/urban sectors were affected

Employment numbers declined sharply in states with high unemployment


🧠 Conclusion


This project demonstrates how Python can be used for time-series analysis, visualization, and economic insights.
Using Pandas, Matplotlib, and Seaborn, I was able to:

Clean and preprocess real-world data

Perform region-wise & timeline-based unemployment analysis

Visualize key economic indicators

Understand COVID-19’s impact through data-driven insights

This task strengthened my skills in
data analysis, visualization, trend interpretation, and storytelling with data.


📁 Files Included


Unemployment_Analysis.ipynb — Complete Google Colab Notebook

README.md — Project documentation

(Optional) Dataset file downloaded via KaggleHub

🙌 Credit

This project is submitted as Task 2 of the
AICTE Oasis Infobyte Internship Program (OIBSIP).
