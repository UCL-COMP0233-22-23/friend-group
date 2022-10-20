"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill" : {
        "age": 26,
        "job": 'biologist',
        'friend': 'Zalika',
        "partner": "John"
    },
    "Zalika" : {
    "name": "Zalika",
    "age": "28",
    "job": "artist",
    "friend": "Jill",
    "partner": ""
    },
    "John" : {
    "name": "John",
    "age": "27",
    "job": "writer",
    "friend": "",
    "partner": "Jill"
    },
    "Nash" : {
    "name": "Nash",
    "age": "34",
    "job": "chef",
    "cousin": "John",
    "landlord": "Zalika"
    }

}
print(my_group)