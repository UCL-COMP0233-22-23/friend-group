"""An example of how to represent a group of acquaintances in Python."""


class Person:
    """Class to describe a person"""
    def __init__(self, name="unknown", age="unknown", job="unknown", relationships="unknown"):
        self.name = name
        self.age = age
        self.job = job
        self.relationships = relationships

    def add_relationship(self, name, relationship):
        """Add a specified relationship between self.name and name. """
        self.relationships[name] = relationship


class Group:

    def __init__(self, people):
        self.names = self.get_names(people)
        self.ages = self.get_ages(people)
        self.jobs = self.get_jobs(people)
        self.relationships = self.get_relationships(people)

    def get_names(self, people):
        return [x.name for x in people]

    def get_ages(self, people):
        return [x.age for x in people]

    def get_jobs(self, people):
        return [x.job for x in people]

    def get_relationships(self, people):
        relationships = {}
        for person in people:
            relationships[person.name] = person.relationships
        return relationships

jill = Person(name="Jill", age=26, job="biologist", relationships={"Zalika": "friend", "John": "partner"})
zalika = Person(name="Zalika", age=28, job="artist", relationships={"Jill": "friend"})
john = Person(name="John", age=27, job="writer", relationships={"Jill": "partner"})
nash = Person(name="Nash", age=34, job="chef", relationships={"Zalika": "landlord"})

group = [jill, zalika, john, nash]

class_of_group = Group(group)

