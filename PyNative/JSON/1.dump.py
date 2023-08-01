import json

"""The json.dump() method (without “s” in “dump”) used to write Python serialized object as JSON formatted data into a file."""

developer = {
    "name": "jane doe",
    "salary": 29000,
    "skills": ["Raspberry pi", "Machine Learning", "Web Development"],
    "email": "JaneDoe@pynative.com",
}

print("Started writing JSON data into a file")
with open(
        'C:/Users/aseka/source/_________LOIC_BI__________/_______Learning__All/SnowFlake/PYTHON/datasets/output/developer.json',
        'w') as write_file_json:
    result = json.dump(developer, write_file_json, indent=4, separators=(", ", ": "), sort_keys=True)
print("Done writing JSON data into .json file")

"""Skip nonbasic types while writing JSON into a file using skipkeys parameter"""
class PersonalInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print("Developer name is " + self.name, "Age is ", self.age)


dev = PersonalInfo("John", 36)
developer_Dict = {
    PersonalInfo: dev,
    "salary": 9000,
    "skills": ["Python", "Machine Learning", "Web Development"],
    "email": "jane.doe@pynative.com"
}
print("Writing JSON data into file by skipping non-basic types")
with open("developer.json", "w") as write_file:
    json.dump(developer_Dict, write_file, skipkeys=True)
print("Done")

"""Handle non-ASCII characters from JSON data while writing it into a file"""

unicode_string = u"\u00f8"
print("unicode String is ", unicode_string)

# set ensure_ascii=False
print("JSON character encoding by setting ensure_ascii=False")
print(json.dumps(unicode_string, ensure_ascii=False))





