class Data():
	def __init__(self):
		self.__data = [1, 2, 3, 4, 5]
	def get_data(self, n):
		self.__data.append(n)
	def print_data(self):
		print(self.__data)

some_data = Data()
some_data.get_data(2)
some_data.print_data()




