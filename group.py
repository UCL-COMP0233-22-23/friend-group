"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    
    "John": {
        "age": 47,
        "occupation": 'Hunk',
        "connection": 'He has been alone for the last 30 years'
    },
    
    "Tony": {
        "age": 60,
        "occupation": 'Don',
        "connection": 'He knows everybody' 
    },

    "Fredo": {
        "age": 32,
        "occupation": 'Consigliere',
        "connection": 'Third in line' 
    },

    "Michael": {
        "age": 51,
        "occupation": 'Underboss',
        "connection": 'He is the heir' 
    },

    "Christopher": {
        "age": 27,
        "occupation": 'Consigliere',
        "connection": 'He\'\s Tonys Nephew' 
    },
}

print(my_group["John"]["age"])

