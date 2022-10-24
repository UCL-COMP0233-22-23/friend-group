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

#summary data from the group
print("The maximum age in the group is: ", max([person["age"] for person in my_group]))
len_relations = [len(person["relations"]) for person in my_group]
print("The average number of relations per person is: ", sum(len_relations) / len(len_relations))
print("The maximum age of people in the group that have >= one relation is: ", max([person["age"] for person in my_group if len(person["relations"]) >= 1]))
print("The maximum age of people in the group that have >= one friend is ", max([person["age"] for person in my_group if len(person["relations"]["friend"]) >= 1]))