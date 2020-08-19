#!usr/bin/env python3

class ETNode:
    '''
    Node of expression tree (binary tree)
    '''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.right)
        print(root.val, end=' ')
        inorder(root.left)

def constructTree(postfix):
    '''
    Construct a binary tree using postfix expression
    :param: postfix: String, postfix expression
    '''
    stack = []
    for el in postfix:
        if el.isalpha():    # character
            stack.append(ETNode(el))
        else:      # operator of tree node
            op1 = stack.pop()
            op2 = stack.pop()
            curr = ETNode(el)
            curr.left = op1
            curr.right = op2
            stack.append(curr)
    
    # prints infix expression of the given postfix expression
    inorder(stack.pop())

postfix = "ab+ef*g*-"
constructTree(postfix)