import requests
import zipfile
import io
import json

# https://gist.github.com/FedericoTartarini/9496282b4b2f508c0ab2da96f4955397
# SOURCE
# Setting user Parameters
api_token = "v8D9Zv0Jlyg84pXR8fgqMiRe0MnuXMsbG1fYWEvy"
file_format = "csv"
data_center = 'yul1'  # "<Organization ID>.<Datacenter ID>"
survey_id = 'SV_2mMFEB1OKln3F9I'
# Setting static parameters
request_check_progress = 0
progress_status = "in progress"
# https://yul1.qualtrics.com/API/v3/surveys/SV_2mMFEB1OKln3F9I/export-responses/413e5919-9abb-46df-b4d7-adf8ad5032da-def/file
# base_url = "https://{0}.qualtrics.com/API/v3/export-responses/".format(data_center)
base_url = 'https://yul1.qualtrics.com/API/v3/surveys/SV_2mMFEB1OKln3F9I/export-responses/'


get_responses_surveys_url = 'https://ca1.qualtrics.com/API/v3/surveys/SV_2mMFEB1OKln3F9I/export-responses/ebba1a47-082d-4d55-9093-dc5af04ec15c-def/file'
headers = {
    "content-type": "application/json",
    "x-api-token": api_token,
}

# Step 1: Creating Data Export
download_request_url = base_url
download_request_payload = '{"format":"' + file_format + '","surveyId":"' + survey_id + '"}'  # you can set useLabels:True to get responses in text format
# print('download_request_payload', download_request_payload)
# download_request_response = requests.request("POST", download_request_url, data=download_request_payload,
#                                              headers=headers)
download_request_response = requests.get(get_responses_surveys_url, headers=headers)

# print('download_request_response', download_request_response.text)
# print("Status Code", download_request_response.status_code)
# print("JSON Response ", download_request_response.json())
download_request_response = download_request_response.json()
# str to json or dict
number_responses_id = len(download_request_response['responses'])
print(f"Number Response ID: {number_responses_id}")
# add responseId to ['responses'][0]['values'] to get all fields's request
download_request_response['responses'][0]['values']['responseId'] = download_request_response['responses'][0]['responseId']

for i in range(number_responses_id):
    print(i)

# print(type(download_request_response))
# print(download_request_response['responses'][0]['values'])

# Create Python object from JSON string data
# obj = json.loads(download_request_response)
# json_formatted_str = json.dumps(obj, indent=4)




# progress_id = download_request_response.json()["result"]["id"]
# print(download_request_response.text)

# # Step 2: Checking on Data Export Progress and waiting until export is ready
# while request_check_progress < 100 and progress_status != "complete":
#     request_check_url = base_url + progress_id
#     request_check_response = requests.request("GET", request_check_url, headers=headers)
#     request_check_progress = request_check_response.json()["result"]["percentComplete"]
#
# Step 3: Downloading file
# request_download_url = base_url + progress_id + '/file'
# request_download = requests.request("GET", request_download_url, headers=headers, stream=True)
request_download_url = get_responses_surveys_url
request_download = requests.request("GET", request_download_url, headers=headers, stream=True)
#
# Step 4: Unzipping the file
path = 'E:\\Bitbucket\\andreloic\\pythonScript'
# zipfile.ZipFile(io.BytesIO(request_download.content)).extractall(path)

print('Downloaded qualtrics survey')


