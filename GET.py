import requests
import pandas as pd
# Outputs dataframe
url = 'http://localhost:5000/sales'

# Query parameters
params = {
    'start_date': '2023-01-01',
    'end_date': '2023-03-31',
    'format': 'json'
}

response = requests.get(url, params=params)

if response.status_code == 200:

    data = response.json()
    df = pd.DataFrame(data)
    print(df)
else:
    print(f"Failed to retrieve data: {response.status_code}")

