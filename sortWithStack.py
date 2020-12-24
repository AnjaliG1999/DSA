#!usr/bin/env python3

class Stack:
    def __init__(self):
        self.res = []       # stack
        
    def push(self, val):
        self.res.append(val)

    def sortArray(self, arr):
        '''
        Sorts List arr using stack
        :param: self: Object
                arr: List
        rtype: List, Result string
        '''
        temp = []       # temporary list to hold greater values
        
        for num in arr:
            # first number in the list
            if not len(self.res):
                self.push(num)
            else:
                if self.res[-1] <= num:
                    self.push(num)
                else:
                    # pop until the top of the stack is less than or equal to num
                    while self.res and self.res[-1] > num:
                        temp.append(self.res.pop())
                    self.push(num)
                    
                    # push the remaining elements into the stack
                    while temp:
                        self.push(temp.pop())
                    
        # return sorted stack (ascending order)
        return self.res

arr = [34, 3, 31, 98, 92, 23]
stack = Stack()
print('Original array: {}'.format(arr))
print('Sorted array: {}'.format(stack.sortArray(arr)))