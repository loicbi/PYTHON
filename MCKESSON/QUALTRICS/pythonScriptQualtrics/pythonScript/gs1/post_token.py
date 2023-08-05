import requests

url = f"https://demo-api-eccnetservices.gs1ca.org/oauth/token"

payload = {"format": "json"}
headers = {
    "Content-Type": "application/json"
}
params = {
    "username": "obapi.demo@Mckesson.ca",
    "grant_type": "password",
    "password": "vBwy74VwLTuqDdfn",
    "client_id": "mckessondemo",
    "client_secret": "7F825CEC-C198-420E-92CD-02D736C33BD5",
    "scope": "basic",
}
# Step 1: Creating Data Export
get_token = requests.request("POST", url, json=payload, params=params,headers = headers)
if get_token.status_code == 200:
    print({
        "status_code":get_token.status_code,
        "get_token":get_token.json(),
    })
else:
    print("Review account config (Username, grant_type, password, client_id, client_secret, scope)")