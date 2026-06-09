# Code 18: Pandas Data Exploration
# Requires: German-Credit_1.csv in the same directory as this script.
# Install: pip install pandas

import pandas as pd

# Load dataset
df = pd.read_csv("German-Credit_1.csv")

# Basic exploration
print(df.head())        # First 5 rows
print(df.head(10))      # First 10 rows
print(df.tail())        # Last 5 rows
print(df.shape)         # (rows, columns)
print(df.columns)       # Column names

# Select a single column as a Series
df1 = df["INSTALL_RATE"]
print(df1.head())

# Data types and null/missing value counts
df.info()
print(df.isnull().sum())

# Descriptive statistics (numeric_only avoids warnings on non-numeric columns)
print(df.mean(numeric_only=True))
print(df.min(numeric_only=True))
print(df["AGE"].mean())
print(df.std(numeric_only=True))
print(df.describe())

# Boolean mask - rows where AMOUNT > 1000
DF2 = (df["AMOUNT"] > 1000)
print(DF2.head())

# iloc - select by integer position
df2 = df.iloc[:, 1:5]      # All rows, columns 1-4
print(df2.head())

# Select first 20 rows and columns 5-11
print(df.iloc[0:20, 5:12])

# loc - select by label
df3 = df.loc[:20, "USED_CAR":"INSTALL_RATE"]
print(df3.head())

# Conditional filtering with multiple conditions
DF2 = df[(df["AMOUNT"] > 1000) & (df["EDUCATION"] == 1)]
print(DF2.head())
