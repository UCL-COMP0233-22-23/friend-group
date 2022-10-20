"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

from statistics import mean


my_group = [
    {
        'name' : 'Jill',
        'age' : 26,
        'job' : 'biologist',
        'connections' : {
            'friend' : 'Zalika',
            'partner' : 'John'
        }
    },
    {
        'name' : 'Zalika',
        'age' : 28,
        'job' : 'artist',
        'connections' : {
            'friend' : 'Jill'
        }
    },
    {
        'name' : 'John',
        'age' : 27,
        'job' : 'writer',
        'connections' : {
            'partner' : 'Jill'
        }
    },
    {
        'name' : 'Nash',
        'age' : 34,
        'job' : 'chef',
        'connections' : {
            'cousin' : 'John',
            'landlord' : 'Zarika'
        }
    }
]

print('The maximum age is ' + str(max(person['age'] for person in my_group)))
print('The mean number of relations is ' + str(mean(len(person['connections']) for person in my_group)))
print('The maximum age of people with at least one relation is ' + str(max(person['age'] for person in my_group if person['connections'])))
print('The maximum age of people with at least one friend is ' + str(max(person['age'] for person in my_group if 'friend' in person['connections'])))
