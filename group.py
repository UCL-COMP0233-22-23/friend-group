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
# the maximum age of people in the group
print("the maximum age of people in the group is ", 
      max([attr["age"] for person, attr in group.items()]))
# the average (mean) number of relations among members of the group
relat = [len(attr["relations"]) for person, attr in group.items()]
print("the average (mean) number of relations among members of the group is ", 
      sum(relat) / len(relat))
# the maximum age of people in the group that have at least one relation
print("the maximum age of people in the group that have at least one relation is ",
      max([attr["age"] for person, attr in group.items() if len(attr["relations"]) >=1]))
# [more advanced] the maximum age of people in the group that have at least one friend
print("the maximum age of people in the group that have at least one friend is ",
      max([attr["age"] for person, attr in group.items() if "friend" in attr["relations"].values()]))
