"""An example of how to represent a group of acquaintances in Python."""

my_dictionary = {'key1': 1, 'key4': 'abc'}
my_dictionary['key1']
my_dictionary['key4']

my_group = {
    'Zhenghao': {
        'name': 'Zhenghao', 
        'age': 22,
        'job': 'a student',
        'relations': 'lanqiming friend',
    }
}

print(my_group['Zhenghao']['name'], 'is', my_group['Zhenghao']['age'])
