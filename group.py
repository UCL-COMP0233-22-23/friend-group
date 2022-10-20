"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    }
    ,"Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    }
    ,
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
age_max = max([int(person['age']) for person in my_group.values()])

# the average (mean) number of relations among members of the group
from numpy import average
relations_mean = average([len(person['relations']) for person in my_group.values()])

# the maximum age of people in the group that have at least one relation
age_max_relations = max([person['age'] for person in my_group.values() if int(len(person['relations']) > 1)])

# [more advanced] the maximum age of people in the group that have at least one friend
age_max_friends = max([person['age'] for person in my_group.values() if 'friend' in person['relations'].values()])

print(age_max_friends)