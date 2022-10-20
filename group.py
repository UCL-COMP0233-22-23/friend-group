"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = "Paul Nathan and Sheila Perez"


class Friend:
    def _init__(self,name,age,job,relations):
        self.name = name
        self.age = age
        self.job = job
        self.relations = {}

    def add_relation(self,friend,relation):
        self.relations[friend] = relation



jill = Friend('Jill','26','Biologist',{'Zalika':'friend','John':'partner'})
zalika = Friend('Zalika','28','Artist',{'Jill':'friend'})
john = Friend('John','27','Writer',{'Jill':'partner'})
nash = Friend('Nash','34','Chef',{'John':'cousin','Zalika':'landlord'})




