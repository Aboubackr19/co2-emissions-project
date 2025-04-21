#!/usr/bin/env python3
import pandas as pd
import sqlite3

conn = sqlite3.connect("db/co2_emissions.db")

# 1. Read cleaned country table
df = pd.read_sql_query("SELECT * FROM country_emissions", conn)
df.to_csv("data/cleaned_co2_emissions.csv", index=False)

conn.close()
print("✔️  Exported cleaned CSV to data/cleaned_co2_emissions.csv")
