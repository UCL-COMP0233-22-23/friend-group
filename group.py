"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    'Jill' : {
        'relationship': {
            'Zalika': 'friend',
            'John': 'partner'
        },
        'age': 26,
        'job': 'Biologist'
    },
    'Zalika' : {
        'relationship': {
            'Jill': 'friend'
        },
        'age': 28,
        'job': 'Artist'
    },
    'John' : {
        'relationship': {
            'Jill': 'partner'
        },
        'age': 27,
        'job': 'Writer'
    },
    'Nash' : {
        'relationship': {
            'John': 'cousin',
            'Zalika': 'landlord'
        },
        'age': 34,
        'job': 'Chef'
    }
}

print(",".join([my_group[x]['job'] for x in my_group]))
