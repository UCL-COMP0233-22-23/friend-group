"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}


import json

json.dumps(group)
print(json.dumps(group, indent=4))

with open('myfile.json', 'r') as json_file:
    my_data_as_string = json_file.read()

# print(my_data_as_string)

mydata = json.loads(my_data_as_string)
print(mydata['somekey'])

