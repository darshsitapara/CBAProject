import requests

url = "http://localhost:5000/sales"
data = {
    "id": 1001,
    "store_id": "TX001",
    "total_sales": 100.00,
    "date": "2023-01-20"
}

response = requests.post(url, json=data)

print(response.text)
