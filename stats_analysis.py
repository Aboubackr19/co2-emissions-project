#!/usr/bin/env python3
import pandas as pd

df = pd.read_csv("data/cleaned_co2_emissions.csv")

# Choose numeric columns by name or dtype
numeric_cols = df.select_dtypes(include="number").columns.tolist()

# 1. Descriptive stats
desc = df[numeric_cols].describe()

# 2. Print to console
print("=== Descriptive statistics for numeric columns ===\n")
print(desc)

# 3. (Optional) save to text file
with open("data/co2_stats.txt", "w") as f:
    f.write(desc.to_string())

print("✔️  Statistics printed and saved to data/co2_stats.txt")
