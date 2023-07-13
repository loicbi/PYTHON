import requests
import json
a = "9dbe93e2-5ff5-4c40-afae-c781a97a6bb3"

# payload =  {"gtins": ["33457900555", "10064541314900"]}
headers = {"Authorization": f"Bearer {a}", 'content-type': 'application/json'}
# url = "https://www.toggl.com/api/v6/" + data_description + ".json"
url = "https://demo-api-contentdistribution.gs1ca.org/api/coverage?ims=ecommerceContent&cursor=0&limits=5"

response = requests.delete(
    url,
    # data=json.dumps(payload),
    headers=headers,
)
a = {'Authorization': 'Bearer "9dbe93e2-5ff5-4c40-afae-c781a97a6bb3"', 'content-type': 'application/json'}

print()
print(response.status_code)