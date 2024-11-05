# test_requests.py
import requests

url = "http://127.0.0.1:8000/predict"
text = "큰거왔다"

response = requests.post(url, json={"text": text})
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
