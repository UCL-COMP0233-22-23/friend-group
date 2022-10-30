"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jack":{
        "age":25,
        "job": "history teacher",
        "relations":{
            "Sam": "friend",
            "Alex":"partner",
            "Zoe": "brother"
        }
    },
    "Sam":{
        "age":27,
         "job": "bartender",
        "relations":{
            "Jack": "friend",
            "Alex": "friend"
        }
    },
    "Zeo":{
        "age":19,
         "job": "student",
        "relations":{
            "Jack": "sister",
        }
    },
    "Alex":{
        "age":22,
        "job": "archeologist",
        "relations":{
            #"Jack": "partner",
            #"Alex": "friend"
        }
    }
}

agelist = []
joblist = []
relation = []
for name, detail in my_group.items():
    agelist += [detail["age"]]
    joblist += [detail["job"]]
    relation += [detail["relations"]]
print(agelist)# print the age, job and relation of people
print(joblist)#But this presentation does not allows people with no key of job or relatoion
print(relation)#It can present the empty key of job and relation
#ages = [properties["age"] for properties in my_group.values()] ---another way
age_of_people_with_many_friends = [properties["age"] for properties in my_group.values() if len(properties["relations"])>=3]
print(age_of_people_with_many_friends)
