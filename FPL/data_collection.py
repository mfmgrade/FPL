# Import necessary libraries
import requests
import pandas as pd

# API endpoints
FPL_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"

# Send a GET request to the FPL API
response = requests.get(FPL_URL)

# Check if the request was successful
if response.status_code != 200:
    raise Exception("Failed to fetch data from FPL API")

# Convert the response to JSON
data = response.json()

# Convert the relevant part of the JSON (in this case, 'elements') to a DataFrame
players_df = pd.DataFrame(data['elements'])

# Save the DataFrame to a CSV file for further use
players_df.to_csv('players_data.csv', index=False, encoding='windows-1252')

