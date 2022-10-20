"""An example of how to represent a group of acquaintances in Python."""

my_group = [{"name":"Jill", 
        "job":"biologist",
        "relationship":[("friend","Zalika"),("partner","John")],
        "age":26},
        {"name":"Zalika", 
        "job":"artist",
        "relationship":[("friend","Jill")],
        "age":28},
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



