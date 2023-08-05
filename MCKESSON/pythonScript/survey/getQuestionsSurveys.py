import requests, sys, collections

if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    from collections.abc import MutableMapping
else:
    from collections import MutableMapping

survey_id = 'SV_6S5ZqosmZgtbTYG' # SV_6S5ZqosmZgtbTYG

url_question = f"https://yul1.qualtrics.com/API/v3/survey-definitions/{survey_id}/questions"

headers = {
    "Content-Type": "application/json",
    "X-API-TOKEN": "v8D9Zv0Jlyg84pXR8fgqMiRe0MnuXMsbG1fYWEvy"
}

response = requests.request("GET", url_question, headers=headers)

# print(response.json()['result']['elements'])

list_1 = response.json()['result']['elements']

# number of question
number_question_by_number = len(response.json()['result']['elements'])
# print(number_question_by_number)
question_id_single_without_choice = []
question_id_array_with_choice = []

for i in range(number_question_by_number):
    # CHECK IF ChoiceOrder EXISTS
    try:
        if 'ChoiceOrder' not in list_1[i].keys():
            # print(f"{list_1[i]['QuestionID']} ::: {list_1[i]['QuestionType']} ::: NA ")
            question_id_single_without_choice.append(list_1[i]['QuestionID'])
        else:
            # print(f"{list_1[i]['QuestionID']} ::: {list_1[i]['QuestionType']} has Choice order => {list_1[i]['ChoiceOrder']} ")
            if list_1[i]['ChoiceOrder'] == []:
                question_id_single_without_choice.append(list_1[i]['QuestionID'])
            else:
                """Multiple questions so increment _n"""
                # print(f"{list_1[i]['QuestionID']} ::QuestionType:: {list_1[i]['Choices']} ::ChoiceOrder:: => {list_1[i]['ChoiceOrder']} ")
                # if list_1[i]['QuestionID'] != 'QID13':
                if list_1[i]['QuestionID']:
                    # print(f"{list_1[i]['QuestionID']} ::: {list_1[i]['QuestionType']} has Choice order => {list_1[i]['ChoiceOrder']} ")
                    for j in range(len(list_1[i]['ChoiceOrder'])):
                        # print(f"{list_1[i]['QuestionID']}_{j + 1}")
                        #     print(list_1[j]['QuestionID'], '###### >', list_1[j]['QuestionType'], len(list_1[j]['ChoiceOrder']))
                        question_id_array_with_choice.append(f"{list_1[i]['QuestionID']}_{j + 1}")
                # else:
                #     print(
                #         f"{list_1[i]['QuestionID']} ::: {list_1[i]['QuestionType']} has Choice order => {list_1[i]['ChoiceOrder']} ")
                #     for j in range(len(list_1[i]['ChoiceOrder'])):
                #         question_id_array_with_choice.append(f"{list_1[i]['QuestionID']}_{j + 1}")


    except KeyError:
        print(list_1[i]['QuestionID'], '@@@@@@@@@@@@@@@@@@@@@@@@ERROR@@@@@@@@@@@@@@@@@@@@@@@@',
              list_1[i]['QuestionType'])

    # try:
    #     # single question DB WITH ChoiceOrder
    #     if (list_1[i]['QuestionType'] == 'DB') and (list_1[i]['ChoiceOrder'] == []):
    #         question_id_single_without_choice.append(list_1[i]['QuestionID'])
    #     # else:
    #     #     # MULTIPLE CHOICE
    #     #     if (len(list_1[i]['ChoiceOrder']) > 0):
    #     #         print(list_1[j]['QuestionID'])
    #     #         # for j in range(len(list_1[i]['ChoiceOrder'])):
    #     #             # if list_1[j]['QuestionID'] not in question_id_single_without_choice:
    #     #             #     print(list_1[j]['QuestionID'], '###### >', list_1[j]['QuestionType'],
    #     #             #           len(list_1[j]['ChoiceOrder']))
    #     #             #     question_id_array_with_choice.append(f"{list_1[i]['QuestionID']}_{j + 1}")
    # except KeyError:
    #     # SINGLE QUESTION TE WITHOUT ChoiceOrder
    #     if (list_1[i]['QuestionType'] == 'TE' and (
    #             list_1[i]['QuestionID'] not in question_id_single_without_choice + question_id_array_with_choice)):
    #         print(list_1[i]['QuestionID'], '@@@>', list_1[i]['QuestionType'])
    #         question_id_single_without_choice.append(list_1[i]['QuestionID'])
    #     print(list_1[i]['QuestionID'], ':::::::>', list_1[i]['QuestionType'])

print(f"question_id_single_without_choice: {question_id_single_without_choice}")
print(f"question_id_array_with_choice: {question_id_array_with_choice}")
all_questions_id = question_id_single_without_choice + question_id_array_with_choice
print(len(all_questions_id))
print((all_questions_id))
