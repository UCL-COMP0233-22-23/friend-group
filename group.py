"""An example of how to represent a group of acquaintances in Python."""


# Your code to go here...
my_group = {"Jill": {"Age": 26, 
            "Job": "biologist", 
            "Relationship": {"Zalika": "friend",
            "John": "partner"}},
            
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

#forget(person1, person2) which removes the connection between two people in the group
#add_person(name, age, job, relations) which adds a new person with the given characteristics to the group
#average_age() which calculates the mean age for the group

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

###Try some of the functions
#add_person("Rongru",24,"Student",{"John": "friend"})

#forget("Jill","Zalika")
#my_group


##Add the following comprehensive relations
#the maximum age of people in the group
#the average (mean) number of relations among members of the group
#the maximum age of people in the group that have at least one relation
#[more advanced] the maximum age of people in the group that have at least one friend

MaxiAge_comprehend = max([info["Age"] for name, info in my_group.items()])
Mean_relation = sum([len(info["Relationship"]) for name, info in my_group.items()])/len(my_group.keys())
MaxAge_relation = max([info["Age"] for name, info in my_group.items() if len(info["Relationship"]) >1])
MaxAge_friend = max([info["Age"] for name, info in my_group.items() if "friend" in info["Relationship"].values()])

