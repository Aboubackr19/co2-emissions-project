#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect("db/co2_emissions.db")
cur  = conn.cursor()

for tbl in ("country_emissions", "global_emissions"):
    # 1. Get column names
    cols = [col[1] for col in cur.execute(f"PRAGMA table_info({tbl})")]
    # 2. Replace NULL with 0
    for col in cols:
        cur.execute(f"""
            UPDATE {tbl}
            SET "{col}" = 0
            WHERE "{col}" IS NULL
        """)
conn.commit()
conn.close()

print("✔️  Cleaned database: NULLs replaced with 0")
