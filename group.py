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

import numpy as np

max_age = max([group[person]["age"] for person in group])
mean_relations = np.average([len(group[person]["relations"]) for person in group])
max_age_min_one_relation = max([group[person]["age"] for person in group if len(group[person]["relations"]) >= 1])
max_age_min_one_friend = max([group[person]["age"] for person in group if "friend" in list(group[person]["relations"].values())])

print("The maximum age of people in the group is " + str(max_age))
print("The mean number of relations is " + str(mean_relations))
print("The maximum age of people with at least one relation is " + str(max_age_min_one_relation))
print("The maximum age of people with at least one friend is " + str(max_age_min_one_friend))