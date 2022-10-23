"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

import collections
class person:
    
    def __init__(self, name, age, job) -> None:
        self.name = name
        self.age = age
        self.job = job
        self.connection = collections.defaultdict(list)
        
    def add_connection(self, friend):
        self.connection[self.name].append(friend)
        
Jill = person('Jill', 27, 'writer')
Jill.add_connection("zalika")
Jill.add_connection('Dave')

Zalika = person('Zalika', 28, 'artist')
Dave = person('Dave', 34, 'driver')

print(Jill.connection)
