#!usr/bin/env python3

# Linked List implementation of stack

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, val):
        '''
        Adds an element to the stack
        :param: self: Object
                val: int, value of the new node
        rtype: None
        '''
        newNode = Node(val)
        newNode.next = self.top
        self.top = newNode
    
    def pop(self):
        '''
        Removes the top element of the stack
        :param: self: Object
        rtype: int
        '''
        if stack.isEmpty():
            print('Stack underflow')
            return
        temp = self.top
        self.top = self.top.next
        return temp.val
        
    def peek(self):
        '''
        Returns the top element of the stack
        :param: self: Object
        rtype: int
        '''
        return self.top.val
    
    def isEmpty(self):
        '''
        Tells whether the stack is empty or not
        :param: self: Object
        rtype: bool
        '''
        return self.top == None
        
    def printStack(self):
        '''
        Prints the stack
        :param: self: Object
        rtype: None
        '''
        temp = self.top
        print('Stack: ', end='')
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
    
stack = Stack()
values = int(input('Enter the number of values to add: '))
print('Add values: ')
for x in range(values):
    val = int(input())
    stack.push(val)

print('Top element: {}'.format(stack.peek()))
print(stack.pop())
stack.printStack()
print('The stack is empty') if stack.isEmpty() else print('The stack is not empty')