import requests
from bs4 import BeautifulSoup

# URL of the CO2 Emissions website
url = "https://example.com/world-co2-emissions"  # Replace with the actual URL

# Send a request to the website to get the raw HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the CO2 emissions data (check the website for the correct table tag or class)
table = soup.find('table')  # Adjust this based on the actual HTML structure

# Extract all rows from the table
rows = table.find_all('tr')

# Create an empty list to store the data
data = []

# Loop through each row to get the column data (td elements)
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]  # Clean up the text and remove extra spaces
    if len(cols) > 0:  # Only append rows that have data (avoid header row)
        data.append(cols)

# Save to CSV (Step 2)
import pandas as pd

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data, columns=['Country', 'CO2 Emissions', 'Year Change', 'Population', 'Per Capita', 'Share of World'])

# Save the DataFrame to a CSV file
df.to_csv('co2_emissions.csv', index=False)
