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

# Saving structure to JSON
import json

print(json.dumps(group))

with open('group-data.json', 'w') as output:
    output.write(json.dumps(group))

# Reading json
group_reload = None
with open('group-data.json', 'r') as input:
    group_reload = input.read()

group_reload = json.loads(group_reload)
print(group_reload)
print(type(group_reload))
assert group_reload == group