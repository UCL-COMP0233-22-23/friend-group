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
                    {"PersonA" : Nash, "PersonB" : Zalika, "RelationType" : "Landlord", "Reciprocal" : False},
                ]
                # added inverse role if reciprocal is false.

# A list of all people
People = [Jill, Zalika, John, Nash] 

# the maximum age of people in the group
max_age = 0
for p in People:
    if p["Age"] > max_age:
        max_age = p["Age"]
print(max_age)

# the average (mean) number of relations among members of the group
def count_relations(person):
    total = 0
    for r in Relationships:
        if r["PersonA"] == person or r["PersonB"] == person:
            total += 1
    return total

total_relations = 0
for p in People:
    total_relations += count_relations(p)

print(total_relations / len(People))

# the maximum age of people in the group that have at least one relation
max_age = 0
for p in People:
    if p["Age"] > max_age and count_relations(p) > 0:
        max_age = p["Age"]
print(max_age)

# the maximum age of people in the group that have at least one friend
def count_friends(person):
    total = 0
    for r in Relationships:
        if (r["PersonA"] == person or r["PersonB"] == person) and r["RelationType"] == "Friend":
            total += 1
    return total

max_age = 0
for p in People:
    if p["Age"] > max_age and count_friends(p) > 0:
        max_age = p["Age"]
print(max_age)
