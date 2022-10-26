"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
            'Jill': {
                'age': 26,
                'job': 'biologist',
                'connections': {
                    'Zalika': 'friend',
                    'John': 'partner'
                    }
            }
            
            , 
            
            'Zalika': {
                'age': 28,
                'job': 'artist',
                'connections': {
                    'Jill': 'friend',
                }
            }, 
            
            'John' : {
                'age': 27,
                'job': 'writer',
                'connections': {
                    'Jill': 'partner',
                    } 
            },
            
            'Nash' : {
                'age': 34,
                'job': 'chef',
                'connections': {
                    'John': 'cousin',
                    'Zalika': 'landlord'
                    } 
            }
            
        
    }
        

def max_age():
    '''max age of people'''
    ages = [my_group[i]['age'] for i in my_group]

    return print(max(ages))


def average_relations():
    '''average number of connections in the group'''
    average=[len(my_group[i]['connections']) for i in my_group] #average number of connections per person
        
    tot_average = sum(average)/len(average) #total average number of relations

    return print(tot_average)


def max_age2():
    '''max age of people with atleast one connection'''
    ages = [my_group[i]['age'] for i in my_group if len(my_group[i]['connections']) >0]

    return print(max(ages))





max_age()
average_relations()
max_age2()