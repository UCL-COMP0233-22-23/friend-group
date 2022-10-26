"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group =[
    
    {
        'name' : 'William',
        'age' : 22,
        'job' : 'programmer',
        'connections' : {
            'son' : 'Jack'
        }
    },
    {
        'name' : 'Jack',
        'age' : 20,
        'job' : 'boss',
        'connections' : {
            'dad' : 'William',
            
        }
    }
]
print(max(person["age"] for person in group.values()))  
print(mean([len(person["relations"]) for person in group.values()]))  
print(max(person["age"] for person in group.values() if person["relations"]))  
print(max(person["age"] for person in group.values() if "friend" in person["relations"].values()))  

