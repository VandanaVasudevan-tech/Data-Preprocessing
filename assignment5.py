import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv('Employee.csv')
df.info()

# 1(a) Explore the data, list down the unique values in each feature and find its length.
for col in df.columns:
    print(f"\nColumn: {col}")
    print("Unique Values:", df[col].unique())
    print("Number of unique values: ", df[col].nunique())

# 1(b) Perform the statistical analysis and renaming of the columns.
# print(df.describe(include='all'))
df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns)

# Find the missing and inappropriate values, treat them appropriately.
missing_values = df.isnull().sum()
print("Missing Values\n", missing_values)

# Replace the value 0 in age as NaN Treat the null values in all columns using any
# measures(removing/ replace the values with mean/median/mode) .
df['age'] = df['age'].replace(0, np.nan)
df['age'].fillna(df['age'].median(), inplace=True)
df['salary'].fillna(df['salary'].mean(), inplace=True)
# Categorical Columns
for col in df.select_dtypes(include='object'):
    df[col].fillna(df[col].mode()[0], inplace=True)
print(df.isnull().sum())

# Removed all duplicate rows.
df = df.drop_duplicates()
print(df.duplicated())

# Find the outliers.
plt.figure(figsize=(5, 4))
plt.boxplot(df['age'])
plt.title('Age Distribution')
plt.show()

plt.figure(figsize=(5, 4))
plt.boxplot(df['salary'])
plt.title('Salary Distribution')
plt.show()
print("""In a boxplot, outliers are identified as individual points outside the whiskers. In this plot, no such points 
are visible, which indicates that no outliers are detected based on the IQR rule. However, plotting variables with very 
different scales together can hide variability, so it’s better to visualize them separately.""")

# IQR - Removes outliers from both columns
for col in ['age', 'salary']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower) & (df[col] <= upper)]

# Data Analysis:
# Filter the data with age >40 and salary<5000 Plot the chart with age and salary
# Count the number of people from each place and represent it visually

filtered_df = df[(df['age'] > 40) & (df['salary'] < 5000)]
print(filtered_df)

# visually inspected the relationship between age and salary after filtering.

plt.figure(figsize=(5, 4))
plt.scatter(filtered_df['age'], filtered_df['salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary (Age > 40 and Salary < 5000)')
plt.show()
place_counts = filtered_df['place'].value_counts()
print(place_counts)

# place count represented visually

plt.figure()
place_counts.plot(kind='bar')
plt.xlabel('Place')
plt.ylabel('Number of People')
plt.title('People Count by Place (Filtered Data)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Data Encoding:
categorical_cols = ['company', 'place', 'country']
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# After the process of encoding, perform the scaling of the features using
# standardscaler and minmaxscaler.

X = df_encoded.copy()

# Standard Scaling
standard_scaler = StandardScaler()
X_standard = X.copy()
X_standard[['age', 'salary']] = standard_scaler.fit_transform(
    X_standard[['age', 'salary']]
)

# Min-Max Scaling
minmax_scaler = MinMaxScaler()
X_minmax = X.copy()
X_minmax[['age', 'salary']] = minmax_scaler.fit_transform(
    X_minmax[['age', 'salary']]
)
df_encoded.to_csv('employee_cleaned_encoded.csv', index=False)