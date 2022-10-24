"""An example of how to represent a group of acquaintances in Python."""

#forget(person1, person2) which removes the connection between two people in the group
def forget(person1, person2):
    for i in range(my_group.__len__()):
        if my_group[i]['name'] == person1 or my_group[i]['name'] == person2:
            relationships = my_group[i]['relationship']
            j = 0
            while j < relationships.__len__():
                if relationships[j][1] == person1 or relationships[j][1] == person2:
                    del(my_group[i]['relationship'][j])

                else: 
                    j = j + 1

#add_person(name, age, job, relations) which adds a new person with the given characteristics to the group
def add_person(name,age,job,relations):
    my_group.append( 
        {"name":name, 
        "job":job,
        "relationship":relations,
        "age":age}
        )

#average_age() which calculates the mean age for the group
def average_age():
    total_group_age = sum([my_group[i]['age'] for i in range(my_group.__len__())])
    total_group_size = my_group.__len__()
    return (total_group_age/total_group_size)

my_group = [
    {"name":"Jill", 
    "job":"biologist",
    "relationship":[("friend","Zalika"),("partner","John")],
    "age":26}
    ,
    {"name":"Zalika", 
    "job":"artist",
    "relationship":[("friend","Jill")],
    "age":28}
    ,
    {"name":"John", 
        "job":"writer",
        "relationship":[("partner","Jill")],
        "age":27},
    {"name":"Nash", 
        "job":"chef",
        "relationship":[("landlord","Zalika"),("cousin","John")],
        "age":34}
    ]

#print(my_group[0]['name'] + " is " + str(my_group[0]["age"]) +", a " + my_group[0]["job"] +" and she is " + my_group[0]['relationship'][0][1] + "'s " + my_group[0]['relationship'][0][0])

#Homework - Anda

#The indices of the dictionnaries representing the data related to friends, for the my_group list.
list = [j for j in range(my_group.__len__())]

#maximum age of ppl in the group
[print(max(age)) for age in [[my_group[i]['age'] for i in list]]]

#the average (mean) number of relations among members of the group
[print(total/my_group.__len__()) for total in [sum([my_group[i]['relationship'].__len__() for i in list])]]

#the maximum age of people in the group that have at least one relation
[print(max(age)) for age in [[my_group[i]['age'] for i in list if my_group[i]['relationship'].__len__()>=1]]]

#[more advanced] the maximum age of people in the group that have at least one friend
[print(max(age)) for age in [[my_group[i]['age'] for i in list if ('friend' in [my_group[i]['relationship'][j][0] for j in range(my_group[i]['relationship'].__len__())])]]]


#Stretch Goal: Friend group data functions 

#Test forget method
forget('Jill','John')
[print(my_group[ind]['relationship']) for ind in list]

#Test add_person method
add_person("Sheldon",30,"pilot",[("friend","Nash")])
updated_list = [j for j in range(my_group.__len__())]
[print(my_group[ind]['name']) for ind in updated_list]

#Test average_age
print(average_age())

