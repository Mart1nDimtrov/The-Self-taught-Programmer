class Orange():
	def __init__ (self, color, size, weight):
		self.color = color
		self.size = size
		self.weight = weight

	def print_orange(self):
		print(self)
		print(self.color)
		print(self.size)
		print(self.weight)


orange = Orange("orange", "10cm", "20lb")
orange.print_orange()