class Mammal():
	def __init__(self, name):
		self.hunger = 100
		self.tired = 100
		self.name = name
	def print_result(self, amount, action):
		print("{} {} decreased by {}.".format(self.name, action, amount))
	def eat(self, decrease):
		self.hunger -= decrease
		self.print_result(decrease, "hunger")
	def sleep(self, decrease):
		self.tired -= decrease
		self.print_result(decrease, "tiredness")

class Dolphin(Mammal):
	pass
class Monkey(Mammal):
	def eat(self, decrease):
		self.hunger -= decrease
		print("Monkey likes bananas!")
class Sloth(Mammal):
	def sleep(self, decrease):
		self.tired -= decrease
		print("Sloth sleeps forever!")
class Tiger(Mammal):
	def sleep(self, decrease):
		self.tired -= decrease
		print("The tiger is really tired!")

dolphin = Dolphin("dolphin")
dolphin.eat(10)
dolphin.sleep(10)
tiger = Tiger("tiger")
tiger.eat(10)
tiger.sleep(10)
monkey = Monkey("monkey")
monkey.eat(10)
monkey.sleep(10)
sloth = Sloth("sloth")
sloth.eat(10)
sloth.sleep(10)

		
