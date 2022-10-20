"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

from numpy import average


my_group = {
    "Jill" : {
        "age": 26,
        "job": "biologist",
        "relations": {
            "friend": "Zalika",
            "partner": "John"
        }
    },
    "Zalika" : {
        "name": "Zalika",
        "age": "28",
        "job": "artist",
        "relations": {
            "friend": "Jill",
            "partner": ""
        }
    },
    "John" : {
        "name": "John",
        "age": "27",
        "job": "writer",
        "relations": {
            "friend": "",
            "partner": "Jill"
        }
    },
    "Nash" : {
        "name": "Nash",
        "age": "34",
        "job": "chef",
        "relations": {
            "friend": "John",
            "landlord": "Zalika"
        }
    }

}

def forget(person1, person2):
    # removes the connection between two people in the group

    # tmp1 = my_group[person1]['relations']
    # tmp2 = my_group[person2]['relations']

    my_group[person1]['relations'] = {k:v for (k,v) in my_group[person1]['relations'].items() if v != person2}
    my_group[person2]['relations'] = {k:v for (k,v) in my_group[person2]['relations'].items() if v != person1}
print('-----------------Before-----------------')
print(my_group)
forget('Jill', 'John')
print('-----------------After-----------------')
print(my_group)


def add_person(name, age, job, relations):
    # adds a new person with the given characteristics to the group
    my_group[name] = {'name': name, 
                        'age': age,
                        'job': job,
                        'relations': relations
                        }
    print(my_group)

# add_person('Scott', 22, 'Student', {'friend': 'yubing'})

def average_age():
    # calculates the mean age for the group

    # tmp = [int(my_group[k]['age']) for k in my_group.keys()]
    # age =  sum(tmp)/len(tmp)

    from numpy import average
    age = average([int(my_group[k]['age']) for k in my_group.keys()])
    print(age)

# average_age()