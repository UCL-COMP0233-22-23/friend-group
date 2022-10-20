"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class People:
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job
        self.relation = []

    def connect(self, name, relationship):
        self.relation.append({'name': name, 'relationship': relationship})
    

jill = People('Jill', 26, 'biologist')
zalika = People('Zalika', 28, 'artist')
john = People('John', 27, 'writer')
nash = People('Nash', 34, 'chef')
jill.connect(zalika.name, 'friend')
jill.connect(john.name, 'partner')
zalika.connect(jill.name, 'friend')
john.connect(jill.name, 'partner')
nash.connect(john.name, 'cousin')


my_group = [jill, zalika, john, nash]

print('here')
