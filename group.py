"""An example of how to represent a group of acquaintances in Python."""

class Person:

	def __init__(self, name, age, job=None):
		self.name = name
		self.job = job
		self.age = age
		self.relationships = []

	def __str__(self):
		out_start = f"{self.name} is {self.age}"
		# optional parameter: job
		if not self.job:
			out_job = ""
		elif self.job[0].lower() in ["a","e","i","o"]:
			out_job = f", an {self.job}"
		else:
			out_job = f", a {self.job}"
		# optional parameter: relationship
		rel_str_list = [f"{self.relationships[i][1]}'s {self.relationships[i][0]}" for i in range(len(self.relationships))]
		if not rel_str_list:
			out_relationship = ""
		elif len(rel_str_list) > 2:
			out_relationship = "; they are " + ", ".join(rel_str_list[:-2]) + ", " + " and ".join(rel_str_list[-2:])
		else:
			out_relationship = "; they are " + " and ".join(rel_str_list)
		return out_start + out_job + out_relationship

	def add_relationship(self, rel_type, person):
		if type(rel_type) in [list, tuple]:
			self.relationships.append((rel_type[0], person.name))
			person.relationships.append((rel_type[1], self.name))
		else:
			self.relationships.append((rel_type, person.name))
			person.relationships.append((rel_type, self.name))

	def forget_relationship(self, person):
		for i, relationship in enumerate(self.relationships):
			if relationship[1] == person.name:
				del self.relationships[i]
		for i, relationship in enumerate(person.relationships):
			if relationship[1] == self.name:
				del person.relationships[i]

def add_person(group, person):
	group += person

def average_age(group):
	ages = []
	for i in group:
		ages.append(i.age)
	return sum(ages)/len(ages)

my_group = []
jill = Person("Jill", 26, "Biologist")
zalika = Person("Zalika", 28, "Artist")
john = Person("John", 27, "Writer")
nash = Person("Nash", 34, "Chef")

add_person(my_group, [jill, zalika, john, nash])

jill.add_relationship("Friend", zalika)
jill.add_relationship("Partner", john)
nash.add_relationship("Cousin", john)
nash.add_relationship(("Landlord", "Tenant"), zalika)

print("\n".join([str(my_group[i]) for i in range(len(my_group))]))
print("The average age of people in the group is", average_age(my_group))

# Exercises
print("The maximum age of people in the group is", max([i.age for i in my_group]))
len_relationships = [len(i.relationships) for i in my_group]
print("The average (mean) number of relations among members of the group is", sum(len_relationships)/len(len_relationships))
print("The maximum age of people in the group that have at least one relation is", max([i.age for i in my_group if len(i.relationships) >= 2]))
print("The maximum age of people in the group that have at least one friend is", max([i.age for i in my_group if len([j[1] for j in i.relationships if j[0] == "Friend"]) >= 1]))