"""An example of how to represent a group of acquaintances in Python."""
# Testing push/pull
# Your code to go here...

my_group = {
    # (name, age) as key
    # ["job", list of relations as tuples (name, relation to name)] as value
    ("Jill", 26):["biologist", ("John", "partner"), ("Zalika", "friend")], 
    ("Zalika", 28):["artist", ("Jill", "friend")],
    ("John", 27):["writer", ("Jill":"partner")],
    ("Nash", 34):["cook", ("John", "cousin"), ("Zalika":"landlord")]
}

# Flexibly dataset to add people with various relations
# Difficulty in searching 
# It allows people with no connections
# Doesn't assume reciprocal relations