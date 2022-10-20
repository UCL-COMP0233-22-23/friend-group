"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group =

'''class Person:
    def _init_(self,Name,age,friend,partner,cousin,tenant):
    self.name = name
    self.age = age
    self.friend = friend
    self.partner = partner
    self.cousin = cousin
    self.tenant = tenant

Jill = Person('Jill','26','biologist','Zalika','John','','')
print(Jill.name)'''

my_group = {['Name':'Jill', 'age':'26','job':'biologist','friend':'Zalika','partner':'John'],['Name':'Zalika','age':'28','job':'artist','friend':'Jill'],['Name':'John','job':'writer','partner':'Jill'],['Name':'Nash','job':'chef','cousin':'John','tenant':'Zalika']}
#print(my_group)