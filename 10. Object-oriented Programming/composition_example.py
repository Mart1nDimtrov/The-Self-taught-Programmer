class Dog():
	def __init__(self, name, breed, owner):
		self.name = name
		self.breed = breed  
		self.owner = owner

class Person():
	def __init__(self, name):
		self.name = name

mick = Person("Jack")
dog = Dog("Joffrey", "pitbull", mick)
print(dog.owner.name)




