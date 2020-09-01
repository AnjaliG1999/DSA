#!usr/bin/env python3

# Create a tree node
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def buildTreePre(preorder, inorder, start, end):
	"""
	Build the tree from the preorder and inorder lists

	:param: preorder: list
			inorder: list
			start: int, first index of the list
			end: int, last index of the list
	:rtype: Node
	"""
	if start > end: return
	
	root = Node(preorder[buildTreePre.preIndex])
	buildTreePre.preIndex += 1
	
	# if current tree is empty
	if not root: return
	
	# leaf nodes of the tree
	if start == end: return root
	
	# find next root in the tree
	index = inorder.index(root.val)
	root.left = buildTreePre(preorder, inorder, start, index-1)
	root.right = buildTreePre(preorder, inorder, index+1, end)
	return root

def buildTreePost(postorder, inorder, start, end):
	"""
	Build the tree from the inorder and postorder lists

	:param: postorder: list
			inorder: list
			start: int, first index of the list
			end: int, last index of the list
	:rtype: Node
	"""
	if start > end: return

	root = Node(postorder[buildTreePost.postIndex])
	buildTreePost.postIndex -= 1

	# if current tree is empty
	if not root: return

	# leaf nodes of the tree
	if start == end: return root

	# find next root in the tree
	index = inorder.index(root.val)
	root.right = buildTreePost(postorder, inorder, index+1, end)
	root.left = buildTreePost(postorder, inorder, start, index-1)
	
	return root

def calculateHeightRec(root):
	"""
	Calculate the height of the tree

	:param: root: Node, Root of the current tree
	:rtype: int
	"""
	if not root: return 0

	return 1 + max(calculateHeight(root.left), calculateHeight(root.right))

def calculateHeightIter(root):
	if not root:
		return 0

	height = 0
	queue = [root]
	while queue:
		size = len(queue)
		while size:
			node = queue.pop(0)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
			size -= 1
		height += 1

	return height

def inOrder(root):
	"""
	Inorder traversal of the tree
	Implemented to check if the tree is built correctly

	:param: root: Node, Root of the current tree
	:rtype: None
	"""
	if root:
		inOrder(root.left)
		print(root.val, end=" ")
		inOrder(root.right)

preorder = [1, 2, 4, 7, 9, 5, 3, 6, 8]
inorder = [7, 9, 4, 2, 5, 1, 3, 6, 8]
postorder = [9, 7, 4, 5, 2, 8, 6, 3, 1]

buildTreePre.preIndex = 0
buildTreePost.postIndex = -1
# root = buildTreePre(preorder, inorder, 0, len(inorder)-1)
root = buildTreePost(postorder, inorder, 0, len(inorder)-1)
inOrder(root)
print()
# print(f'Height of the tree: {calculateHeightRec(root)}')
print(f'Height of the tree: {calculateHeightIter(root)}')