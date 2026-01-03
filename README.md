# Data-Preprocessing
📌 Project Overview

This project focuses on data preprocessing, cleaning, analysis, encoding, and feature scaling using an employee dataset.
The goal is to prepare high-quality data suitable for machine learning and data analysis by handling missing values, outliers, categorical variables, and feature scaling.

📂 Dataset

File: Employee.csv

Description: Contains employee-related information such as age, salary, company, place, and country.

🛠️ Technologies Used

	  Python
	  
	  NumPy
	  
	  Pandas
	  
	  Matplotlib
	  
	  Scikit-learn

🔍 Project Workflow

1️⃣ Data Exploration

  Loaded the dataset using Pandas
  
  Displayed dataset structure using df.info()

Identified:

Unique values per column

Number of unique entries in each feature

2️⃣ Data Cleaning & Preprocessing

Renamed columns to lowercase and replaced spaces with underscores

Identified missing values

Treated invalid and missing data:

Replaced 0 values in age with NaN

Filled missing age values using median

Filled missing salary values using mean

Filled missing categorical values using mode

Removed duplicate records

3️⃣ Outlier Detection and Treatment

Visualized outliers using boxplots for:

Age



<img width="620" height="502" alt="image" src="https://github.com/user-attachments/assets/e9bb73ff-1f76-403f-a026-f447d8b31664" />




Salary



<img width="613" height="507" alt="image" src="https://github.com/user-attachments/assets/85436add-bd68-4d84-851a-1189a4670f08" />





Applied Interquartile Range (IQR) method to remove outliers from numerical columns

4️⃣ Data Analysis & Visualization

Filtered employees with:

age > 40

salary < 5000

Visualized:

Age vs Salary using a scatter plot


<img width="743" height="505" alt="image" src="https://github.com/user-attachments/assets/11d0a3a5-55c2-4b63-bd22-f2eb1ed2d7af" />



Number of employees by place using a bar chart


<img width="795" height="606" alt="image" src="https://github.com/user-attachments/assets/8cdf83a1-2196-4236-882d-106c459bd929" />




5️⃣ Categorical Encoding

Converted categorical variables into numerical format using One-Hot Encoding

Encoded columns:

company

place

country

Used drop_first=True to avoid multicollinearity

6️⃣ Feature Scaling

Applied StandardScaler to normalize age and salary

Applied MinMaxScaler to rescale age and salary between 0 and 1

Updated the scaled values directly in the encoded DataFrame

7️⃣ Exporting Cleaned Data

Saved the final cleaned, encoded, and scaled dataset to:

employee_cleaned_encoded.csv

| File Name                    | Description                          |
| ---------------------------- | ------------------------------------ |
| Employee.csv                 | Original dataset                     |
| employee_cleaned_encoded.csv | Cleaned, encoded, and scaled dataset |




🚀 Key Learnings

Importance of data cleaning before analysis

Handling missing and invalid values effectively

Outlier detection using IQR

One-Hot Encoding for categorical variables

Feature scaling using StandardScaler and MinMaxScaler



📌 Conclusion

This project demonstrates a complete data preprocessing pipeline, making the dataset ready for machine learning models and further statistical analysis.
