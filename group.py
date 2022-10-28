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


def forget(person1, person2):
    for name, info in my_group.items():
        RelationDic = info["Relationship"]
        if name == person1:
            RelationDic.pop(person2, None)
        if name == person2:
            RelationDic.pop(person1, None)

def add_person(name, age, job, relations = {}):
    my_group[name] = {"Age": age, "Job": job, "Relationship": relations }
    
def average_age():
    age = 0
    count_num = 0
    for name, info in my_group.items():
        age += info["Age"]
        count_num += 1
    average = age/count_num
    print(f"The average age of {count_num} people in the group is {average}")

 