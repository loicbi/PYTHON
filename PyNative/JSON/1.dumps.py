import json

"""The json.dumps() method encodes any Python object into JSON formatted String."""


def dumps_sendJsonResponse(resultDict: dict) -> str:  # or dumps_sendJsonResponse(resultDict)
    print('''Convert Python dictionary into JSON formatted String''')
    result = json.dumps(resultDict, indent=4, sort_keys=True)
    return result


# sample developer dict
developer_Dict = {
    "name": "Jane Doe",
    "salary": 9000,
    "skills": ["Python", "Machine Learning", "Web Development"],
    "email": "jane.doe@pynative.com"
}
print(dumps_sendJsonResponse(developer_Dict))
