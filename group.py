"""An example of how to represent a group of acquaintances in Python."""

class friend_group():
    def __init__(self,name,age,job,connection):
        self.name = name
        self.age = age
        self.job = job
        self.connection = connection
        
friend1 = friend_group('Wei',21,'Student',['Maruf friend','Random'])
friend2 = friend_group('Maruf',21,'Student','Weis friend')

friend1.name
