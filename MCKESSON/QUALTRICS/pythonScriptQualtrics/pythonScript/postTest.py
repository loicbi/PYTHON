import requests
import zipfile
import io
from datetime import datetime
import requests

survey_id = 'SV_4NPoN9SryGI8hb8'
api_token = "v8D9Zv0Jlyg84pXR8fgqMiRe0MnuXMsbG1fYWEvy"

startDate = '2010-01-01T00:00:00Z'
endDate = '2023-12-31T00:00:00Z'

url = f"https://yul1.qualtrics.com/API/v3/surveys/{survey_id}/export-responses"

payload = {"format": "json",
           "startDate": startDate,
           "endDate": endDate,
           "compress": False, }
headers = {
    "Content-Type": "application/json",
    "X-API-TOKEN": api_token,
}
# Step 1: Creating Data Export
get_ProgressId = requests.request("POST", url, json=payload, headers=headers).json()['result']['progressId']

print(get_ProgressId)
# https://yul1.qualtrics.com/API/v3/surveys/SV_2mMFEB1OKln3F9I/export-responses/ES_6kWBjbYTzJmEDEW
url_progressId = f"https://yul1.qualtrics.com/API/v3/surveys/{survey_id}/export-responses/{get_ProgressId}"

request_check_progress = 0.0
progress_status = "in progress"
# request_check_response = requests.request("GET", url_progressId, headers=headers)
# request_check_progress = request_check_response.json()["result"]["percentComplete"]
# print(request_check_response.json())
# print(request_check_progress)
get_FileId = dict()
# Step 2: Checking on Data Export Progress and waiting until export is ready
while request_check_progress < 100 and progress_status != "complete":
    request_check_response = requests.request("GET", url_progressId, headers=headers)
    request_check_progress = request_check_response.json()["result"]["percentComplete"]
    get_FileId = request_check_response.json()
get_FileId = get_FileId["result"]['fileId']

get_responses_surveys_url = f"https://ca1.qualtrics.com/API/v3/surveys/{survey_id}/export-responses/{get_FileId}/file"
print(get_responses_surveys_url)
# # Step 3: Downloading file
# # 'https://ca1.qualtrics.com/API/v3/surveys/SV_2mMFEB1OKln3F9I/export-responses/ebba1a47-082d-4d55-9093-dc5af04ec15c-def/file'
# request_download_url = url_progressId + '/file'
# request_download = requests.request("GET", request_download_url, headers=headers, stream=True)
#
# # Step 4: Unzipping the file
# zipfile.ZipFile(io.BytesIO(request_download.content)).extractall(dir_save_survey)
# print('Downloaded qualtrics survey')


# a = '2023-03-12T21:27:50Z'
# print(type(a))
# a = datetime.strptime(a, "%Y-%m-%dT%H:%M:%SZ")
# print(a)
# print(type(a))


