class Node():
	"""Class representing one node in a linked list."""
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None

class LinkedList():
	"""Class representing a linked list data structure"""
	def __init__(self, head):
		self.head = head

	def add(self, data):
		"""Add a new node to the linked list."""
		previous_head = self.head
		self.head = Node(data)
		previous_head.previous = self.head
		self.head.next = previous_head


node = Node(1)
linked_list = LinkedList(node)
linked_list.add(2)
linked_list.add(3)

node = linked_list.head
while node:
	print(node.data)
	node = node.next

