#!usr/bin/env python3

# Tree node object
class Node:
	def __init__(self, key):
		self.parent = None
		self.left = None
		self.right = None
		self.key = key

# node insertion in a tree
def node_insert(root, newNode):
	node = None
	tempRoot = root

	# find the parent of newNode
	while tempRoot:
		node = tempRoot
		if newNode.key < tempRoot.key:
			tempRoot = tempRoot.left
		else:
			tempRoot = tempRoot.right
		
	# linking the two nodes
	newNode.parent = node
		
	if not node:		#tree is empty
		root = newNode
	elif newNode.key < node.key:
		node.left = newNode
	else:
		node.right = newNode

sum1 = 0
addedValues = []
# modified inorder tree traversal		
def modifiedInorder(node):
	global sum1
	if node:
		modifiedInorder(node.right)
		sum1 += node.key
		addedValues.insert(0, sum1)
		modifiedInorder(node.left)
		
root = Node(20)
bstNodes = [30, 40, 50, 60, 70, 80]
for val in bstNodes:
	node_insert(root, Node(val))

modifiedInorder(root)
print(addedValues)