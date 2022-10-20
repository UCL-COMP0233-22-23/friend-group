"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill" : {
        "age": 26,
        "job": "biologist",
        "connection": {
            "friend": "Zalika",
            "partner": "John"
        }
    },
    "Zalika" : {
    "name": "Zalika",
    "age": "28",
    "job": "artist",
    "connection": {
        "friend": "Jill",
        "partner": ""
        }
    },
    "John" : {
    "name": "John",
    "age": "27",
    "job": "writer",
    "connection": {
        "friend": "",
        "partner": "Jill"
        }
    },
    "Nash" : {
    "name": "Nash",
    "age": "34",
    "job": "chef",
    "connection": {
        "friend": "John",
        "landlord": "Zalika"
        }
    }

}
# print(my_group)

class person:
    def __init__(self,name, age, job=None):
        self.name = name
        self.age = age
        self.job = job
        self.relation = {}

    def add_relation(self, name, relationship):
        self.relation[relationship] = name

Jill = person('Jill', 26, 'biologist')
Jill.add_relation('Zalika', 'friend')
Jill.add_relation('John', 'partner')

Zalika = person('Zalika', 28, 'artist')
Zalika.add_relation('Jill', 'friend')

John = person('John', 27, 'writer')
John.add_relation('Jill', 'partner')

Nash = person('Nash', 34, 'Chef')
Nash.add_relation('John', 'Cousin')
Nash.add_relation('Zalika', 'landlord')
print(Nash.relation)