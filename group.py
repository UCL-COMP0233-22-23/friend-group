"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = "Paul Nathan and Sheila Perez"


class Friend:
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job
        self.relations= {}

    def add_relation(self,friend,relation):
        self.relations[friend] = relation

    def get_age(self):
        return self.age

    def get_job(self):
        return self.job 

    def get_relations(self):
        return self.relations 



jill = Friend('Jill','26','Biologist')
zalika = Friend('Zalika','28','Artist')
john = Friend('John','27','Writer')
nash = Friend('Nash','34','Chef')

jill.add_relation('Zalika','friend')
jill.add_relation('John','partner')
zalika.add_relation('Jill','friend')
john.add_relation('Jill','partner')
nash.add_relation('John','cousin')
nash.add_relation('Zalika','landlord')


