import json

data = {
    
    "name" : "Paulo",
     "age" : 29,
    "city" : "Dasma Cavite"
}

# convert to json string
json_string = json.dumps(data)
print("JSON string:", json_string)

# convert back to python dict
parsed_data = json.loads(json_string)
print("Parsed data:",parsed_data)