"""An example of how to represent a group of acquaintances in Python."""

import numpy as np

# Your code to go here...
'''
class Person:
    def __init__(self,name,age,job,relationship):
        self.name = name
        self.age = age
        self.job = job
        self.relationship = relationship

Jill = Person('Jill','26','biologist',[['friend','Zalika'],['partner','John']])
Zalika = Person('Zalika','28','artist',[['friend','Jill']])
John = Person('John','writer',[['partner','Jill']])
Nash = Person('Nash','34','chef',[['cousin','John'],['tenant','Zalika']])

print(Jill.name)
print(Jill.relationship)
print(Jill.job)
'''

my_group = {
    'Jill':{'age':26,'job':'biologist','relationship':{'friend':'Zalika','partner':'John'}},
    'Zalika':{'age':28,'job':'artist','relationship':{'friend':'Jill'}},
    'John':{'age': 27,'job':'writer','relationship':{'partner':'Jill'}},
    'Nash':{'age':34,'job':'chef','relationship':{'cousin':'John','tenant':'Zalika'}}
}

#print(my_group)

#maxage = max(my_group, key=lambda dic:dic['age'])
#print(maxage['age'])

numrel = 0
maxage = 0
i = 0


for name, person in my_group.items():
    #print("name: ", name, ", age:", person['age'], ", relation: ")
    #print(len(person['relationship']))
    numrel = numrel + len(person['relationship'])
    i = i + 1
    if person['age']>maxage:
        maxage = person['age']
        maxname = name
        if len(person['relationship'])>1:
            relname = name
        for rel in person['relationship']:
            if rel == 'friend':
                friname = name


print("max age: ", maxage)
print("avg relations: ", numrel/i)

print("the maximum age of people in the group that have at least one relation: ", relname)
print("the maximum age of people in the group that have at least one friend: ", friname)