"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


# my_group = {'TianYi': [22,"google algorithm engineer"], 'houkang': [21,"boss"], 'jiahe': [23,"rocket engineer"]}

my_group = {
    'tianyi' : {
        'relationship': {
            'younger brother' : 'houkang',
            'elder brother' : 'jiahe',
        },
        'age' : 22,
        'job' : "google algorithm engineer"
    },
    'houkang' : {
        'relationship': {
            'elder brother' : 'tianyi',
            'elder brother' : 'jiahe',
        },
        'age' : 21,
        'job' : "ikun leader"
    },
    'jiahe' : {
        'relationship': {
            'younger brother' : 'tianyi',
            'younger brother' : 'houkang',
        },
        'age' : 23,
        'job' : "rocket engineer"
    },
}

# my_group = {
#     'tianyi' : {
#         'relationship': {
#             'brother' : ['jiahe','houkang']
#         },
#         'age' : 22,
#         'job' : "google algorithm engineer"
#     },
#     'houkang' : {
#         'relationship': {
#             'brother' : ['tianyi','jiahe']
#         },
#         'age' : 21,
#         'job' : "ikun leader"
#     },
#     'jiahe' : {
#         'relationship': {
#             'brother' : ['tianyi','houkang'],
#         },
#         'age' : 23,
#         'job' : "rocket engineer"
#     },
# }