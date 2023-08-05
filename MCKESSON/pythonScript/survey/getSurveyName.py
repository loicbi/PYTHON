import requests
import re
survey_id = 'SV_8jC7Blg2OEmwhp4'
url = f"https://ca1.qualtrics.com/API/v3/surveys/{survey_id}"

# url = f"https://yul1.qualtrics.com/API/v3/survey-definitions/{survey_id}"


headers = {
    "Content-Type": "application/json",
    "X-API-TOKEN": "v8D9Zv0Jlyg84pXR8fgqMiRe0MnuXMsbG1fYWEvy"
}

response = requests.request("GET", url, headers=headers)
print(response.json())
surveyName = response.json()['result']['name']
# surveyName = response.json()['result']['SurveyOptions']['SurveyTitle']

# surveyName = "                     @@@ gdgyhd dggbdyhd - hgdyjhd(246152115-12-44                  )"

print(surveyName)
surveyName = re.sub(r"[^A-Za-z0-9]", " ", surveyName).rstrip().lstrip().replace("  ", "").replace(' ', '_').upper()
print(surveyName)
exit()

import re
a = '''NPS Survey - Medicine Shoppe (FR)'''
b = ''

for k in a.split("\n"):
    print(re.sub(r"[^a-zA-Z0-9]+", '_', k))
    b = re.sub(r"[^a-zA-Z0-9]+", '_', k)

if b[-1] == '_':
    b = b.rstrip(b[-1])
print(f"b: {b}")