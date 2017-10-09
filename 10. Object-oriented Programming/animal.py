class Animal():
	def __init__ (self, name):
		self.hunger = 100
		self.tired = 100
		self.name = name

	def print_result(self, amount, action):
		print("{} {} decreased by {}." .format(self.name, action,
		 amount))

	def eat (self, decrease):
		self.tired -= decrease
		self.print_result(decrease, 'hunger')

	def sleep (self, decrease):
		self.tired -= decrease
		self.print_result(decrease, 'tiredness')

class Bear(Animal):
	pass

class Kangaroo(Animal):
	def jump(self, high):
		print("{} jumped {} meters." .format(self.name, high))

class Horse(Animal):
	def __init__ (self, name, speed):
		Animal.__init__ (self, name)
		self.speed = speed

	def run(self):
		print("{} runs with {} kilometers per hour." 
			.format(self.name, self.speed))

class Shark(Animal):
	def __init__ (self, name, speed, dangerous):
		Animal.__init__ (self, name)
		self.speed = speed
		self.dangerous = dangerous

	def eat(self, decrease):
		if (self.dangerous):
			print("Don't feed the shark!") 
		else:
			super().eat(decrease)


roger = Kangaroo("Roger")
roger.jump(5)

bojack = Horse("Bojack", 10)
bojack.run()

panda = Bear("Pandy")
panda.eat(10)

white_shark = Shark("Sharky", 40, True)
white_shark.eat(10)

tiger_shark = Shark("Sharky", 40, False)
tiger_shark.eat(10)





		 



