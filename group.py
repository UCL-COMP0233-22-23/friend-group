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
#the maximum age of people in the group
ages = []
for i in group:
    age = group[i]['age']
    ages.append(age)
print("the maximum age of people in the group:", max(ages))

#the average (mean) number of relations among members of the group
rel_nums = 0
for i in group:
    rel_num = len(group[i]['relations'])
    rel_nums +=rel_num
ave_num = rel_nums / len(group)
print("the average (mean) number of relations among members of the group:", ave_num)

#the maximum age of people in the group that have at least one relation
ages = []
for i in group:
    if len(group[i]['relations']) >= 1:
        age = group[i]['age']
        ages.append(age)
print("the maximum age of people in the group that have at least one relation", max(ages))

#the maximum age of people in the group that have at least one friend
ages = []
for i in group:
    if 'friend' in group[i]['relations'].values():
        age = group[i]['age']
        ages.append(age)
print("the maximum age of people in the group that have at least one friend", max(ages))
