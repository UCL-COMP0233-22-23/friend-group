from statistics import mean


group = {
    
    "John" : {
    'age' : 21,
    'job' :'student',
    'connection' : {"Ann": "friend", "B":"friend"} 
    }, 

    "Ann" : {
    'age' : 20,
    'job' : 'student',
    'connection' : {"John":" friend"}
    },
    
    "Nash": {
    "age": 34,
    "job": "chef",
    "connection": {"John": "cousin", "Zalika": "landlord"}
    },
    
    "Zalika": {
    "age": 28,
    "job": "artist",
    "connection": {"Ann": "cousin"}
    },
}

# the maximum age of people in the group
ages = [i["age"] for i in group.values()]
print("The maximum age of people in the group is", max(ages))

# the average (mean) number of relations among members of the group
num_relation = [len(i["connection"]) for i in group.values()]
mean_relation = mean(num_relation)
print("The average (mean) number of relations among members of the group is", mean_relation)

# the maximum age of people in the group that have at least one relation
age_rel = [i["age"] for i in group.values() if len(i["connection"]) >= 1]
print("the maximum age of people in the group that have at least one relation is",max(age_rel))

#  the maximum age of people in the group that have at least one friend
age_friend = [i["age"] for i in group.values() if "friend" in i["connection"].values()]
print("the maximum age of people in the group that have at least one friend is", max(age_friend))