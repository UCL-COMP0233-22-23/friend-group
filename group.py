"""An example of how to represent a group of acquaintances in Python."""

from hashlib import new


my_group = {
    'Jill': {
        'age': 26,
        'job': ['biologist'],
        'connections': {
            'Zalika': 'friend',
            'John': 'partner'
        }},
    'Zalika': {
        'age': 28,
        'job': ['artist'],
        'connections': {
            'Jill': 'friend',
            'Nash': 'tenant'
        }},
    'John': {
        'age': 27,
        'job': ['writer'],
        'connections': {
            'Jill': 'partner',
            'Nash': 'cousin'
        }},
    'Nash': {
        'age': 34,
        'job': ['chef'],
        'connections': {
            'John': 'cousin',
            'Zalika': 'landlord'
        }}
}

def forget(person1, person2):
    """person1 and person2 are names as strings"""
    if person1 in my_group[person2]['connections'].keys():
        del my_group[person2]['connections'][person1]
    if person2 in my_group[person1]['connections'].keys():
        del my_group[person1]['connections'][person2]

def add_person(group, name, age, job, relations):
    """group = defined variable, name, job = string, age = number, relations = dictionary"""
    group[name] = {}
    group[name]['age'] = age
    group[name]['job'] = [job]
    group[name]['connections'] = relations
    for newrelation in group[name]['connections'].keys(): #this ensures that connections are made both ways
        if newrelation in my_group.keys():
            my_group[newrelation]['connections'][name] = group[name]['connections'][newrelation]

def average_age(group):
    """group is a dictionary of people where age is a key"""
    age = 0
    for person in group.keys():
        age += group[person]['age']
    print('The average age is {0:.2f} years'.format(age/len(group)))

average_age(my_group)