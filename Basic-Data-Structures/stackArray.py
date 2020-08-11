#!usr/bin/env python3

# Array implementation of stack
# maximum capacity of the stack
CAPACITY = int(input('Enter maximum capacity of the stack: '))
stack = []

def push(stack, val):
    '''
    Adds an element to the stack
    :param: stack: List
    rtype: None
    '''
    global CAPACITY, elements
    if elements == CAPACITY:
        print('Stack overflow')
        return
    
    stack.append(val)
    # stack.insert(0, val)
    elements += 1

def pop(stack):
    '''
    Removes the top element of the stack
    :param: stack: List
    rtype: int
    '''
    global CAPACITY, elements
    if isEmpty(stack):
        print('Stack underflow')
        return
    
    elements -= 1
    return stack.pop()
    # return stack.pop(0)

def peek(stack):
    '''
    Returns the top element of the stack
    :param: stack: List
    rtype: int
    '''
    return stack[-1]

def isEmpty(stack):
    '''
    Tells whether the stack is empty or not
    :param: stack: List
    rtype: bool
    '''
    return len(stack)==0

values = int(input('Enter the number of values to add: '))
print('Add values: ')
elements = 0
for x in range(values):
    val = int(input())
    push(stack, val)

print(stack)
print('Element popped: {}'.format(pop(stack)))
print('Top element: {}'.format(peek(stack)))
print('The stack is empty') if isEmpty(stack) else print('The stack is not empty')