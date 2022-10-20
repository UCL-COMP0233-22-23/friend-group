"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = "harveymannering-OscarCharlieST"


"""
    Each person in the group has a name. 
    Each person in the group has an age.
    Each person in the group can have a job.
    Each person can be connected to others in different ways, such as "friend", "granddaughter", "colleague" etc.
"""

# Each person has their own dictionary
Jill = {
    "Name" : "Jill",
    "Age" : 26,
    "Job" : "Biologist"
}

Zalika  = {
    "Name" : "Zalika",
    "Age" : 28,
    "Job" : "Artist",

        
}

John = {
    "Name" : "John",
    "Age" : 27,
    "Job" : "Writer",

}

Nash  = {
    "Name" : "Nash",
    "Age" : 34,
    "Job" : "Chef",
}


# List of all "Relationships"
Relationships = [
                    {"PersonA" : Jill, "PersonB" : Zalika, "RelationType" : "Friend", "Reciprocal" : True},
                    {"PersonA" : Jill, "PersonB" : John, "RelationType" : "Partner", "Reciprocal" : True},
                    {"PersonA" : Nash, "PersonB" : John, "RelationType" : "Cousin", "Reciprocal" : True},
                    {"PersonA" : Nash, "PersonB" : Zalika, "RelationType" : "Landlord", "Reciprocal" : False, 'Inverse' : 'Tenant'},
                ]
                # added inverse role if reciprocal is false.
