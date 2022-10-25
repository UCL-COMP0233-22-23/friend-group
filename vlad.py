
from unicodedata import name


people = {
    'acquaintances': [
        {
            'id': 1,
            'name': 'Jill',
            'age': 26,
            'job': 'Constructor'
        },
        {
            'id': 2,
            'name': 'Zalika',
            'age': 28,
            'job': 'Developer'
        },
        {
            'id': 3,
            'name': 'John',
            'age': 27,
            'job': 'Developer'
        }
    ],
    'relationships': [
        {
            'id': 1,
            'type': 'friend',
            'acquaintance1': 1,
            'acquaintance2': 2
        }
    ]
}