"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
 
names = ['Jill', 'Zalika', 'John', 'Nash']
ages = [26, 28, 27, 34]
jobs = ['biologist', 'artist', 'writer', 'chef']
networks = [{'friend': 'Zalika', 'partner': 'John'},
{'friend': 'Jill'},
{'partner': 'Jill'},
{'cousin':'John', 'landlord':'Zalika'}]

my_group = []

def add_people(names, ages, jobs, networks):
    for i in range(len(names)):
        my_group.append({ 'name': names[i], 'age': ages[i], 'job': jobs[i], 'network': networks[i]})
    return my_group

people = add_people(names, ages, jobs, networks)
print(people)



