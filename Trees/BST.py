#!usr/bin/env python3

#Tree node object
class Node:
	def __init__(self, key):
		self.parent = None
		self.left = None
		self.right = None
		self.key = key

#node insertion in a tree
def node_insert(root, newNode):
	node = None
	tempRoot = root

	#find the parent of newNode
	while tempRoot:
		node = tempRoot
		if newNode.key < tempRoot.key:
			tempRoot = tempRoot.left
		else:
			tempRoot = tempRoot.right
		
	#linking the two nodes
	newNode.parent = node
		
	if node is None:		#tree is empty
		root = newNode
	elif newNode.key < node.key:
		node.left = newNode
	else:
		node.right = newNode

#replace a node with another
def trasplant(root, toRemove, toReplace):
	if toRemove.parent is None:
		root = toReplace
	elif toRemove == toRemove.parent.left:
		toRemove.parent.left = toReplace
	else:
		toRemove.parent.right = toReplace
	
	if toReplace:
		toReplace.parent = toRemove.parent

#node deletion in a tree
def node_delete(root, toDelete):
	if toDelete.left is None:
		trasplant(root, toDelete, toDelete.right)
	elif toDelete.right is None:
		trasplant(root, toDelete, toDelete.left)
	else:
		#replaced the node with a node having value greater than
		#the deleted node in the program
		#can be replaced with a node with lesser value
		treeMin = tree_minimum(toDelete.right)
		if treeMin.parent is not toDelete:
			trasplant(root, treeMin, treeMin.right)
			treeMin.right = toDelete.right
			treeMin.right.parent = treeMin
		
		trasplant(root, toDelete, treeMin)
		treeMin.left = toDelete.left
		treeMin.left.parent = treeMin

#print preorder tree traversal
def preorder(node):
	if node:
		print(node.key, end=" ")
		preorder(node.left)
		preorder(node.right)

#print inorder tree traversal		
def inorder(node):
	if node:
		inorder(node.left)
		print(node.key, end=" ")
		inorder(node.right)

#print postorder tree traversal
def postorder(node):
	if node:
		postorder(node.left)
		postorder(node.right)
		print(node.key, end=" ")

#search a key in the tree
def tree_search(root, value):
	if root is None or value is root.key:
		return root
	if root.key > value:
		return tree_search(root.left, value)
	else:
		return tree_search(root.right, value)

#find the minimum value present in the tree
def tree_minimum(node):
	while node.left:
		node = node.left
	return node

#find the maximum value present in the tree
def tree_maximum(node):
	while node.right:
		node = node.right
	return node

#find a node's successor value (the smallest value greater than the node)
def successor(node):
	if node.right:
		return tree_minimum(node.right)
	pnode = node.parent
	while pnode is not None and node is pnode.right:
		node = pnode
		pnode = pnode.parent
	return pnode

#find a node's predecessor value (the largest value lesser than the node)
def predecessor(node):
	if node.left:
		return tree_maximum(node.left)
	pnode = node.parent
	while pnode is not None and node is pnode.left:
		node = pnode
		pnode = pnode.parent
	return pnode

#create a new tree with a predefined root node
root = Node(12)
print("Tree has only the root element with key value 12.")

#add node(s) to the tree
addNodes = int(input("Enter the number of nodes you want to add: "))
print("Enter the values")
for val in range(addNodes):
	node_insert(root, Node(int(input())))

#delete node(s) from the tree
delNodes = int(input("Enter the number of nodes you want to delete: "))
print("Enter the values")
for val in range(delNodes):
	toDelete = int(input())
	valueNode = tree_search(root, toDelete)
	if valueNode:
		node_delete(root, valueNode)
		print(str(toDelete) + " deleted from the tree.")
	else:
		print(str(toDelete) + " is not in the tree, it cannot be deleted.")

#tree traversal and printing the node values
print("Preorder tree traversal")
preorder(root)

print("\nInorder tree traversal")
inorder(root)

print("\nPostorder tree traversal")
postorder(root)

print()

#search for a value in the tree
currentNodeValue = int(input("Search a particular value in the tree: "))
if tree_search(root, currentNodeValue):
	print(str(currentNodeValue) + " is present in the tree!")

	#if node present, find its successor and predecessor
	valueNode = tree_search(root, currentNodeValue)
	if successor(valueNode):
		print("Successor of " + str(currentNodeValue) + " is " + str(successor(valueNode).key))
	else:
		print(str(currentNodeValue) + " has no successor")

	if predecessor(valueNode):
		print("Predecessor of " + str(currentNodeValue) + " is " + str(predecessor(valueNode).key))
	else:
		print(str(currentNodeValue) + " has no predecessor")
		
else:
	print(str(currentNodeValue) + " is not present in the tree..")

#print the smallest and the largest value in the tree
print("Minimum value in the tree is " + str(tree_minimum(root).key))
print("Maximum value in the tree is " + str(tree_maximum(root).key))