# Python JSON :
#     Json is a file that is use to transfer a data between a system or from one place to another. 
#     It is a lightweight data interchange format that is easy for humans to read and write, 
#         and easy for machines to parse and generate. JSON stands for JavaScript Object Notation, 
#         and it is often used in web applications to send data between a server and a client.
#     We need to import json library to work with json objects in python.

#     Syntax :
#         {
#             key: value,
#             key:[
#                 key:value
#             ]
#         }

#     Example :
import json

jsonValue = '{"name": "John", "age": 30, "city": "New York"}'
print(type(jsonValue))

convertedJson = json.loads(jsonValue)
print(convertedJson)

name = convertedJson['age']
print(name)

# Convert dictionary to json format
dict = {
    "name" : "John",
    "age" : 30,
    "city" : "New York",
    "email_Id":"test@gmail.com"
}

print(type(dict))

convertToJSON = json.dumps(dict,indent=4)
print(convertToJSON)
print(type(convertToJSON))

# Load data from json file into python.
with open("json_sample.json","r") as file:
    data = json.load(file)
    print(data)
    print(data["age"])

# Load data from python into json file.
with open("data.json","w") as filewrite:
    json.dump(dict,filewrite,indent=4)

# List to json
list = ["apple", "banana", "cherry"]

convertJson = json.dumps(list,indent=4)
print(convertJson)