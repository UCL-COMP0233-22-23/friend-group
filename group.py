"""An example of how to represent a group of acquaintances in Python."""


# Your code to go here...

my_group = {"Jill": {"Age": 26, 
            "Job": "biologist", 
            "Relationship": {"Zalika": "friend",
            "partner": "John"}},
            
            "Zalika": {"Age": 28, 
            "Job": "artist", 
            "Relationship": {"Jill": "friend"}},

            "John": {"Age": 28,
            "Job": "writer",
            "Relationship": {"Jill": "partner"}},

            "Nash": {"Age": 34,
            "Job": "chef",
            "Relationship": {"John": "cousin", 
            "Zalika": "landlord"}}}
