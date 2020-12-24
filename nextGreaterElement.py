#!usr/bin/env python3

class Stack:
    def __init__(self):
        self.stack = []
        self.nge = {}
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return ''
    
    def findNGE(self, arr):
        '''
        Given an array, find the Next Greater Element (NGE) for every element
        :param: self: Object
                arr: List
        :rtype: Dictionary, Containing NGEs of all elements of arr
        '''
        for num in arr:
            # first element
            if not self.stack:
                self.push(num)
            
            else:
                if num > self.stack[-1]:
                    self.nge[self.pop()] = num
                self.push(num)
        
        while self.stack:
            self.nge[self.pop()] = -1
        
        return self.nge

arr = [11, 13, 21, 3]
stack = Stack()
print('Original array: {}'.format(arr))
print('Sorted array: {}'.format(stack.findNGE(arr)))