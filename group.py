"""An example of how to represent a group of acquaintances in Python."""
# Testing push/pull
# Your code to go here...

my_group = {
    # (name, age) as key
    # ["job", list of relations as tuples (name, relation to name)] as value
    ("Jill", 26):["biologist", ("John", "partner"), ("Zalika", "friend")], 
    ("Zalika", 28):["artist", ("Jill", "friend")],
    ("John", 27):["writer", ("Jill","partner")],
    ("Nash", 34):["cook", ("John", "cousin"), ("Zalika","landlord")]
}

# Flexibly dataset to add people with various relations
# Difficulty in searching 
# It allows people with no connections
# Doesn't assume reciprocal relations

# Find maximum age
max_age, max_age_person = None, None
people = [x[0] for x in my_group.keys()]
ages = [x[1] for x in my_group.keys()]
max_age = max(ages)
max_age_people = people[ages.index(max_age)]

print('Find maximum age')
print(max_age, max_age_people)

# Find mean no. connections in the group
mean_no_connections = None
no_connections = [len(x[1:]) for x in my_group.values()]
mean_no_connections = sum(no_connections)/len(my_group.keys())
print('Find mean no. connections')
print(mean_no_connections)

# Find maximum age with at least one relation

max_age2, max_age_person2 = None, None

# Find people with at least one connection
people_conditioned = [person for person in people if no_connections[people.index(person)]>0]
# Filter ages according to one-connection conditions
ages_conditioned = [age[1] for age in my_group.keys() if age[0] in people_conditioned ]
#print(people_conditioned, ages_conditioned)
max_age2 = max(ages_conditioned)
max_age_person2 = people[ages_conditioned.index(max_age2)]
print('Find people with at least one relation')
print(max_age2, max_age_person2)

# Find maximum age with at least one relation

max_age3, max_age_person3 = None, None

# Find relations for each person
relations = [my_group[person][1:] for person in my_group.keys()]
#print(relations)

# Find no_friends
no_friends = relations
for index, relation in enumerate(relations):
    no_friends[relations.index(relation)] = 0
    for relation_sub in relation:
        if relation_sub[1] == 'friend':
            no_friends[index] += 1

#print(no_friends)
# Find people with at least one friendship

people_conditioned2 = [person for person in people if no_friends[people.index(person)]>0]

# Filter ages according to one-friendship conditions

ages_conditioned2 = [age[1] for age in my_group.keys() if age[0] in people_conditioned2 ]

max_age3 = max(ages_conditioned2)
max_age_person3 = people[ages_conditioned2.index(max_age3)]
print('Find people with at least one friend')
print(max_age3, max_age_person3)

