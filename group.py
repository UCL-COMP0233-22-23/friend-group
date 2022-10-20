"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
group = {
    "Jill" : {"name":"Jill", 
            "age":26, "job":"a biologist", 
            "connction":{
            "friend": "Zalika",
            "partner":"John"}
    },
    "Zalika" : {"name":"Zalika", 
            "age":28, "job":"an artist", 
            "connection":{
                "friend": "Jill",
                "rent":"Nash"}
    },
    "John" : {"name":"John",
            "age":27,
            "job":"a writer",
            "connection":{
                "partner":"Jill",
                "cousin":"Nash"}
    },
    "Nash" : {"name":"Nash",
            "age":34, "job":"a chef", 
            "connection":{
                "cousin":"John", 
                "landlord":"Zalika"}
    }
}

#print(group)

#for i in range(len(group)):
#    print(group[i]['name'],"is",group[i]['age'],",",group[i]['job'], 'and')

print(group.keys())













