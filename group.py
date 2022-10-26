from distutils.file_util import write_file
import json

"""An example of how to represent a group of acquaintances in Python."""

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




#USE OF JASON FILES
with open('my_group.json','w') as infile:
    json.dump(my_group,infile,indent=4)
    "Created the input file"
with open('my_group.json') as infile_test:
    my_group_string = infile_test.read()
   
#print(json.dumps(my_group))
#print(json.dumps(my_group,indent=4))
print(my_group_string)
print('\n')

# Method can be used to parse a valid JSON string and convert it into a Python Dictionary.
my_group_test = json.loads(my_group_string) 

print(my_group_test[0])
print('\n')
print(my_group[1]['job'])
print('\n')
print(my_group_test)
