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


#1. Maximum age of people in the group
age = []
for name, person in group.items():
    age.append(person["age"])
print('Maximum age of people in the group is: ', max(age))
# OR
max_age = max([person["age"] for name, person in group.items()])
print('Maximum age of people in the group is: ', max_age)


#2. The average (mean) number of relations among members of the group
relations_no = []
for name, person in group.items():
    relations_no.append(len(person["relations"]))
print('Average no of relations among members is: ', sum(relations_no)/len(name))
# OR
mean_rel = sum(len(person["relations"]) for name, person in group.items())/len(name)
print('Average no of relations among members is: ', mean_rel)


#3. The maximum age of people in the group that have at least one relation
age_array1 = []
for name, person in group.items():
    if len(person["relations"]) >= 1:
        age_array1.append(person["age"])
print('The max age of people that have at least one relation is: ', max(age_array1))
# OR
max_age_rel = max([person["age"] for name, person in group.items() if len(person["relations"]) >= 1])
print('The max age of people that have at least one relation is: ', max_age_rel)

# 4. [more advanced] The maximum age of people in the group that have at least one friend
age_array2 = []
for name, person in group.items():
    if "friend" in person["relations"].values():
        age_array2.append(person["age"])
print('The max age of people that have at least one friend is: ', max(age_array2))
#  OR
max_age_friend = max([person["age"] for name, person in group.items() if "friend" in person["relations"].values()])
print('The max age of people that have at least one friend is: ', max_age_friend)
