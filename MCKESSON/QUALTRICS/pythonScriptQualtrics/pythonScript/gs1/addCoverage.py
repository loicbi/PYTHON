import requests
import json

url = f"https://demo-api-contentdistribution.gs1ca.org/api/coverage"
a = 'ecommerceContent+pharmaceuticalContent+planoContent+marketingContent'
params = {
    "ims": a,
}
body = {
    "keys": [
        {
            "gtin": 62600201003
        }

    ]
}

authToken = "bf1bb9bc-2627-442d-9ca0-34f73ec452d0"
headers = {
    'Authorization': 'Bearer ' + authToken,
    'Content-Type': 'application/json'
}

response = requests.post(url, json=body, headers=headers)
print(response.status_code)
