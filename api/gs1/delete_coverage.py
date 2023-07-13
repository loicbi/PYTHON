import requests
import json




payload = {'some': 'data'}
headers = {"Authorization": "Bearer MYREALLYLONGTOKENIGOT", 'content-type': 'application/json'}
# url = "https://www.toggl.com/api/v6/" + data_description + ".json"
url = "https://demo-api-contentdistribution.gs1ca.org/api/coverage?ims=ecommerceContent&cursor=0&limits=5"

response = requests.delete(
    url,
    data=json.dumps(payload),
    headers=headers,
)
