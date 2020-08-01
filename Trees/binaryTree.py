#!usr/bin/env python3

# Create a tree node
class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def buildTree(preorder, inorder, start, end):
	"""
	Build the tree from the preorder and inorder lists

	:param: preorder: list
			inorder: list
			start: int, first index of the list
			end: int, last index of the list
	:rtype: Node
	"""
    if start > end:
        return
    
    root = Node(preorder[buildTree.preIndex])
    buildTree.preIndex += 1
    
    # if current tree is empty
    if not root:
        return
    
    # leaf nodes of the tree
    if start == end:
        return root
    
    # find next root in the tree
    index = inorder.index(root.val)
    root.left = buildTree(preorder, inorder, start, index-1)
    root.right = buildTree(preorder, inorder, index+1, end)
    return root

def inOrder(root):
	"""
	Inorder traversal of the tree

	:param: root: Node, Root of the current tree
	:rtype: None
	"""
    if root:
        inOrder(root.left)
        print(root.val, end=" ")
        inOrder(root.right)

preorder = [1, 2, 4, 7, 9, 5, 3, 6, 8]
inorder = [7, 9, 4, 2, 5, 1, 3, 6, 8]

buildTree.preIndex = 0
root = buildTree(preorder, inorder, 0, len(inorder)-1)
inOrder(root)