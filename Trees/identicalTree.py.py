#!usr/bin/env python3

# Create a tree node
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def isIdentical(tree1, tree2):
	# if both nodes are null
	if not tree1 and not tree2:
		return True

	# if both nodes are not null and the root values are identical
	if (tree1 and tree2) and (tree1.val == tree2.val):
		return isIdentical(tree1.left, tree2.left) and isIdentical(tree1.right, tree2.right)

# construct first tree
x = Node(15)
x.left = Node(10)
x.right = Node(20)
x.left.left = Node(8)
x.left.right = Node(12)
x.right.left = Node(16)
x.right.right = Node(25)

# construct second tree
y = Node(15)
y.left = Node(10)
y.right = Node(20)
y.left.left = Node(8)
y.left.right = Node(12)
y.right.left = Node(16)
y.right.right = Node(25)

if isIdentical(x, y):
	print('The binary trees are the same')
else:
	print('The binary trees are not the same')