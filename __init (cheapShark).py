import requests
import json
import pandas as pd

url = "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"

payload={}
headers = {}

# Gets the list of deals
response = requests.request("GET", url, headers=headers, data=payload).text

# Loads the data into a Python readable dictionary
response_info = json.loads(response)

# Writes to a JSON file
with open('./data.json', 'w', encoding='utf-8') as f:
    json.dump(response_info, f, ensure_ascii=False, indent=4)

response_info[1]

# Alternative way to get API data direct from the URL
requests.get(url).json()

# Print data
print(response_info)

