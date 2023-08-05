###
# Variables are directly accessible: 
#   print (myvar)
# Updating a variable:
#   context.updateVariable('myvar', 'new-value')
# Grid Variables are accessible via the context:
#   print (context.getGridVariable('mygridvar'))
# Updating a grid variable:
#   context.updateGridVariable('mygridvar', [['list','of'],['lists','!']])
# A database cursor can be accessed from the context (Jython only):
#   cursor = context.cursor()
#   cursor.execute('select count(*) from mytable')
#   rowcount = cursor.fetchone()[0]
###
import requests
import zipfile
import io
from datetime import datetime
import requests

survey_id =  'SV_2mMFEB1OKln3F9I' #'${jv_surveyId}' #'SV_2mMFEB1OKln3F9I'
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

print('get_ProgressId', get_ProgressId)
# https://yul1.qualtrics.com/API/v3/surveys/SV_2mMFEB1OKln3F9I/export-responses/ES_6kWBjbYTzJmEDEW
url_progressId = f"https://yul1.qualtrics.com/API/v3/surveys/{survey_id}/export-responses/{get_ProgressId}"

request_check_progress = 0.0
progress_status = "in progress"
get_FileId = dict()
# Step 2: Checking on Data Export Progress and waiting until export is ready
while request_check_progress < 100 and progress_status != "complete":
    request_check_response = requests.request("GET", url_progressId, headers=headers)
    request_check_progress = request_check_response.json()["result"]["percentComplete"]
    get_FileId = request_check_response.json()
    print(request_check_progress, get_FileId)

context.updateVariable('jv_progressId', get_ProgressId)
context.updateVariable('jv_fieldId', get_FileId['result']['fileId'])
context.updateVariable('jv_status', get_FileId['result']['status'])
context.updateVariable('jv_percentComplete', get_FileId['result']['percentComplete'])