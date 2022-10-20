"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {"Jill": {"Age": 26,"Job": ["biologist"], "Relationships":{"Zalika": "friend", "John": "partner"}}}

my_group["Zalika"] = {"Age": 28, "Job":["artist"],"Relationships":{"Jill":"friend"}}
my_group["John"] = {"Age": 27, "Job":["writer"],"Relationships":{"Jill":"partner"}}
my_group["Nash"] = {"Age": 34, "Job":["chef"],"Relationships":{"John":"cousin", "Zalika": "landlord"}}


