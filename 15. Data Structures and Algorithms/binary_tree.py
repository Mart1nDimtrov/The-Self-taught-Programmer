class TreeNode():
	"""Binary tree node."""
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None

class BinaryTree():
	"""This class represents a binary tree data structure."""
	def __init__(self, root):
		"""
		:param root: Binary tree node
		"""
		self.root = root

def breadth_first(tree):
	"""Breadth first search of binary tree print out each node.
	:param root: BinaryTree
	"""
	current_level = [tree.root]
	next_level = []
	while current_level:
		for node in current_level:
			print(node.value)
			if node.left_child:
				next_level.append(node.left_child)
			if node.right_child:
				next_level.append(node.right_child)
		current_level = next_level
		next_level = []

tree = BinaryTree(TreeNode("a"))
tree.root.left_child = TreeNode("b")
tree.root.right_child = TreeNode("c")
tree.root.left_child.left_child = TreeNode("d")
tree.root.right_child.right_child = TreeNode("e")
breadth_first(tree)


