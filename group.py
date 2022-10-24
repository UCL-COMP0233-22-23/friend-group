"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "friend":"Zalika",
            "partner":"John"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "friend":"Jill",
            "partner":""
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "friend":"",
            "partner":"Jill"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "friend":"",
            "partner":"",
            "cousin":"John",
            "landlord":"Zalika" 
        }
}
}

print(my_group)