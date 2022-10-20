"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

people = {
    "Name": ["Jill","Zalika","John","Nash"],
    "Age": ["26","28","27","34"],
    "Job":["biologist","writer","artist","chef"],
    "Friend":["Zalika","Jill","",""],
    "Partner":["John","","Jill",""],
    "Cousin":["","","Nash","John"],
    "Landlord":["","","","Zalika"]
}
# for value in people.items():
#     #print value
#     print(len([item for item in value if item]))

# for value in people:
for i in range(4):  
    for key in people:
        if people[key][i] == "":
            continue
        else: 
            print(key,": ", people[key][i])
    print("")
