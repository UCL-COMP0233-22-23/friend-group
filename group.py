"""An example of how to represent a group of acquaintances in Python."""
class Person:
  def __init__(self, name, age, connection={},job=None):
    self.name = name
    self.age = age
    self.job=job
    self.connection=connection
    
    
    
Jill=Person('Jill',26,{'friend':'Zalika','partner':'John'},'biologist')
Zalika=Person('Zalika',28, {'friend':'Jill'},'artist')


my_group =[Jill,Zalika]

