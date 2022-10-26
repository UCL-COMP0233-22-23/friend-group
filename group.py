"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

import numpy as np

name = ['Jill','Zalika','John','Nash']
my_group = {'Jill':{'age':26, 'job':'biologist', 'relationship':{'Zalika':'friend','John':'partner'}}, 'Zalika':{'age':28, 'job':'artist', 'relationship':{'Jill':'friend'}}, 'John':{'age':27, 'job':'writer', 'relationship':{'Jill':'partner'}}, 'Nash':{'age':34, 'job':'chef', 'relationship':{'John':'cousin','Zalika':'landlord'}}}

ages=[]
numrel=0
maxage=0

for i in range(len(name)):
    ages.append(my_group[name[i]]['age'])
    numrel+=len(my_group[name[i]]['relationship'])
    

maxage=max(ages)
print(maxage)

print(numrel/len(name))

maxage_1relation = 0
ages_1relation = []

maxage_1friend = 0
ages_1friend = []

for i in range(len(name)):
    if len(my_group[name[i]]['relationship'])>=1:
        ages_1relation.append(my_group[name[i]]['age'])
        
maxage_1relation = max(ages_1relation) 
print(maxage_1relation)
    
for i in range(len(name)):
    if 'friend' in my_group[name[i]]['relationship'].values():
        ages_1friend.append(my_group[name[i]]['age'])

maxage_1friend = max(ages_1friend) 
print(maxage_1friend)




