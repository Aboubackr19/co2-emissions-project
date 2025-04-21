#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("plots", exist_ok=True)
df_ct = pd.read_csv("data/cleaned_co2_emissions.csv")
df_gl = pd.read_csv("data/raw_global_emissions.csv")

# 1) Global CO₂ over time
plt.figure()
plt.plot(df_gl["Year"], df_gl["CO2 emissions (tons, 2022)"], marker="o")
plt.title("Global CO₂ Emissions by Year")
plt.xlabel("Year"); plt.ylabel("Emissions (tons)")
plt.tight_layout()
plt.savefig("plots/global_emissions.png")
plt.close()

# 2) Top 10 emitters (2022)
top10 = df_ct.nlargest(10, "CO2 emissions (tons, 2022)")
plt.figure()
plt.bar(top10["Country"], top10["CO2 emissions (tons, 2022)"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 CO₂-Emitting Countries (2022)")
plt.tight_layout()
plt.savefig("plots/top10_countries.png")
plt.close()

# 3) Pie chart: share of world (top 5)
labels = top10["Country"].iloc[:5]
sizes  = top10["Share of World"].iloc[:5].astype(float)
plt.figure()
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Share of World CO₂ Emissions (Top 5)")
plt.tight_layout()
plt.savefig("plots/share_world_top5.png")
plt.close()

print("✔️  Plots saved in plots/")
