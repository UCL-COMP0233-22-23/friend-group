def forget(person1, person2):
    # person1 is the main human who is forgetting person2
    for person in my_group:
        if person['name'] == person1:
            for connection in person['connections']:
                if person['connections'][connection] == person2:
                    del person['connections'][connection]
                    break

def add_person(name, age, job, connections):
    my_group.append(
        {
            'name' : name,
            'age' : int(age),
            'job' : job,
            'connections' : connections
        }    
    )

def average_age():
    total = 0
    for person in my_group:
        total += person['age']
    return total/len(my_group)

my_group = [
    {
        'name' : 'Jill',
        'age' : 26,
        'job' : 'biologist',
        'connections' : {
            'friend' : 'Zalika',
            'partner' : 'John'
        }
    }
]

forget('Jill', 'John')
add_person('Rachel', '22', '', {})
print(my_group)
print(average_age())