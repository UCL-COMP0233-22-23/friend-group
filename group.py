"""An example of how to represent a group of acquaintances in Python."""
class Person:
  def __init__(self, name, age, connection={},job=None):
    self.name = name
    self.age = age
    self.job=job
    self.connection=connection
    
    
    
Jill=Person('Jill',26,{'friend':'Zalika','partner':'John'},'biologist')
Zalika=Person('Zalika',28, {'friend':'Jill'},'artist')
John=Person('John',27,{'partner':'Jill'},'writer')
Nash=Person('Nash',34,{'cousin':'John','landlord':'Zalika'},'chef')


my_group =[Jill,Zalika,John,Nash]


def forget(person1, person2):
  pass

# which removes the connection between two people in the group
def add_person(name, age, job, relations):
  pass

# which adds a new person with the given characteristics to the group
def average_age():
  pass
# which calculates the mean age for the group

