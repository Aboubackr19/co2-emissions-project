
---

## 4. `scripts/scrape_co2.py`

```python
#!/usr/bin/env python3
import os
import requests
import pandas as pd

# 1. Ensure data folder exists
os.makedirs("data", exist_ok=True)

# 2. Download page and parse tables
URL = "https://www.globalcarbonatlas.org/en/CO2-emissions"
resp = requests.get(URL)
resp.raise_for_status()
tables = pd.read_html(resp.text, flavor="lxml")

# 3. Identify tables by index (may need to adjust)
country_df = tables[0]   # country breakdown
global_df  = tables[1]   # historical global totals

# 4. Save raw CSVs
country_df.to_csv("data/raw_co2_emissions.csv", index=False)
global_df.to_csv("data/raw_global_emissions.csv", index=False)

print("✔️  Scraped and saved raw CSVs to data/")
