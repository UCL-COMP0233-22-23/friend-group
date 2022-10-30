"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jack":{
        "age":25,
        "job": "history teacher",
        "relations":{
            "Sam": "friend",
            "Alex":"partner",
            "Zoe": "brother"
        }
    },
    "Sam":{
        "age":27,
         "job": "bartender",
        "relations":{
            "Jack": "friend",
            "Alex": "friend"
        }
    },
    "Zeo":{
        "age":19,
         "job": "student",
        "relations":{
            "Jack": "sister",
        }
    },
    "Alex":{
        "age":22,
         "job": "archeologist",
        "relations":{
            "Jack": "partner",
            "Alex": "friend"
        }
    }
}
