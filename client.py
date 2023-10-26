import requests
import json
# Define the API endpoint
api_url = 'http://localhost:5000/prediction'
api_url1 = 'http://localhost:5000/stats'


response = requests.get(api_url1)
# Check the response
if response.status_code == 200:
    statistics = response.json()
    print(statistics)
else:
    print('Error:', response.status_code) 
response = requests.post(api_url, json=data)
# Check the response
if response.status_code == 200:
    statistics = response.json()
    print(statistics)
else:
    print('Error:', response.status_code)