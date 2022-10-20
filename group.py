"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

#my_group =

class Person:
    def __init__(self,name,age,job,relationship):
        self.name = name
        self.age = age
        self.job = job
        self.relationship = relationship

Jill = Person('Jill','26','biologist',[['friend','Zalika'],['partner','John']])

print(Jill.name)
print(Jill.relationship)
print(Jill.job)
#my_group = {['Name':'Jill', 'age':'26','job':'biologist','friend':'Zalika','partner':'John'],['Name':'Zalika','age':'28','job':'artist','friend':'Jill'],['Name':'John','job':'writer','partner':'Jill'],['Name':'Nash','job':'chef','cousin':'John','tenant':'Zalika']}
#print(my_group)