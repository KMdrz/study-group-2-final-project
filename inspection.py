import pandas as pd
import numpy as np

# Load datasets
df_a = pd.read_excel("TABLE 1 - Basic Literate Population.xlsx", header=None)
df_b = pd.read_excel("TABLE 2 - Literacy Level Above 5.xlsx", header=None)
df_c = pd.read_excel("TABLE 3 - Functional Literate Population.xlsx", header=None)
df_d = pd.read_excel("TABLE 4 - Literacy Level Above 10.xlsx", header=None)

# Inspect dataset A
print("\n=== Dataset A ===")
print("Shape:", df_a.shape)
print(df_a.head(20).to_string())
print("\nData types:")
print(df_a.dtypes)
print("\nMissing values:")
print(df_a.isnull().sum())
print("Duplicates:", df_a.duplicated().sum())

# Inspect dataset B
print("\n=== Dataset B ===")
print("Shape:", df_b.shape)
print(df_b.head(20).to_string())
print("\nData types:")
print(df_b.dtypes)
print("\nMissing values:")
print(df_b.isnull().sum())
print("Duplicates:", df_b.duplicated().sum())

# Inspect dataset C
print("\n=== Dataset C ===")
print("Shape:", df_c.shape)
print(df_c.head(20).to_string())
print("\nData types:")
print(df_c.dtypes)
print("\nMissing values:")
print(df_c.isnull().sum())
print("Duplicates:", df_c.duplicated().sum())

# Inspect dataset D
print("\n=== Dataset D ===")
print("Shape:", df_d.shape)
print(df_d.head(20).to_string())
print("\nData types:")
print(df_d.dtypes)
print("\nMissing values:")
print(df_d.isnull().sum())
print("Duplicates:", df_d.duplicated().sum())