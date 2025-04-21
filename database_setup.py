#!/usr/bin/env python3
import os
import sqlite3
import pandas as pd

# 1. Load raw CSVs
country_df = pd.read_csv("data/raw_co2_emissions.csv")
global_df  = pd.read_csv("data/raw_global_emissions.csv")

# 2. Ensure db folder exists
os.makedirs("db", exist_ok=True)

# 3. Create & connect to SQLite
conn = sqlite3.connect("db/co2_emissions.db")

# 4. Write two tables
country_df.to_sql("country_emissions", conn, if_exists="replace", index=False)
global_df.to_sql("global_emissions",  conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("✔️  Database created at db/co2_emissions.db with two tables")
