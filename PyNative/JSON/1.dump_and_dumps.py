import json

"""The json.dumps() method encodes any Python object into JSON formatted String."""


def dumps_sendJsonResponse(resultDict:dict) -> str:  # or dumps_sendJsonResponse(resultDict)
    print('''Convert Python dictionary into JSON formatted String''')
    result = json.dumps(resultDict)
    return result


# sample developer dict
developer_Dict = {
    "name": "Jane Doe",
    "salary": 9000,
    "skills": ["Python", "Machine Learning", "Web Development"],
    "email": "jane.doe@pynative.com"
}
print(dumps_sendJsonResponse(developer_Dict))



"""The json.dump() method (without “s” in “dump”) used to write Python serialized object as JSON formatted data into a file."""

developer = {
    "name": "jane doe",
    "salary": 9000,
    "skills": ["Raspberry pi", "Machine Learning", "Web Development"],
    "email": "JaneDoe@pynative.com",
}

print("Started writing JSON data into a file")
with open('C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/PYTHON/datasets/output/developer.json', 'w') as write_file_json:
    result = json.dump(developer, write_file_json, indent=4, separators=(", ", ": "), sort_keys=True)
print("Done writing JSON data into .json file")



