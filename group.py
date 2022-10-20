"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
#Jill is 26, a biologist and she is Zalika's friend and John's partner.
#Zalika is 28, an artist, and Jill's friend
#John is 27, a writer, and Jill's partner.
#Nash is 34, a chef, John's cousin and Zalika's landlord


from tempfile import tempdir


class teammate:
    def __init__(self, name, age, job, connection):
        self.name = name
        self.age = age  # Note the default argument, occupants start empty
        self.job = job
        self.connection = connection

Jill=teammate('Jill',26,'biologist','Zalika\'s friend and John\'s partner')

#Zalika is 28, an artist, and Jill's friend
Zalika=teammate('Zalika',28,'artist','Jill\'s friend')
#John is 27, a writer, and Jill's partner.
John=teammate('John',27,'writer','Jill\'s parterner')
#Nash is 34, a chef, John's cousin and Zalika's landlord
Nash=teammate('Nash',34,'chef','John\'s cousin and Zalika\'s landlord')
