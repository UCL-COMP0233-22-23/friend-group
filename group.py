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

def forget(person1, person2):
    my_group[person1]["relations"][person2] = ""
    my_group[person2]["relations"][person1] = ""
    return my_group

def add_personal(name, age, job, relations):
    my_group.append({"name":name, "age":age, "job":job, "relations":relations})
    return my_group

def average_age():
    age = 0
    for person in my_group:
        age += person["age"]
    return age / len(my_group)