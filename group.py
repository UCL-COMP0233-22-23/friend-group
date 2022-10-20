"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
def bidirectionalset(person1, person2, relationtype):
    person2.relationship[relationtype].append(person1.name)
class Person:
    def __init__(self, name ,age, job):
        self.name = name
        self.age = age
        self.job = job
        self.relationship = {'partner':[],'landlord':[],'friend':[],'cousin':[]}

    def set_relation(self, person,relationtype):
        self.relationship[relationtype].append(person.name)
        bidirectionalset(self,person,relationtype)
jill = Person('Jill',26,'biologist')
zalika = Person('Zalika',28,'artist')
john = Person('John',27,'writer')
nash = Person('Nash',34,'chef')
# person1 = Person('YihanZhang',22, 'Student')
# person2 = Person('LongwenHu',22,'Student')
# person1.set_relation(person2,'partner')
jill.set_relation(zalika,'friend')
jill.set_relation(john,'partner')
nash.set_relation(john,'cousin')
nash.set_relation(zalika,'landlord')
print(jill.relationship)
print(zalika.relationship)
print(john.relationship)
print(nash.relationship)
# def person(name, age, job):
#
#     return {'Name':name, 'Age':age, 'Job':job}
#
# print(my_group =[person("YihanZhang,22,Studnet"),person("LongwenHu,22,Studnet")])
