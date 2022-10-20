#An example of how to represent a group of acquaintances in Python.

friends_dict = {
  "Name": ["Jill", "Zalika", "John", "Nash"],
  "Age": [26, 28, 27, 34],
  "Job": ["Biologist", "Artist", "Writer", "Chef"],
  "Connection": ["Zalika's friend and John's partner", "Jill's friend,", "Jill's Partner", "John's cousin and Zalika's landlord"],
}

#my_group =
for i in range(len(friends_dict)):
    for key in friends_dict:
        print(key, friends_dict[key][i])
        if friends_dict[key][i] == "": # break empty list space
                break
print("")