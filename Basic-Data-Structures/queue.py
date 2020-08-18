#!usr/bin/env python3

class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity    # maximum queue capacity
        
    def findFront(self):
        '''
        Return the front element of queue
        :param: self: Object
        :rtype: None/ int
        '''
        if self.isEmpty():
            return
        return self.queue[0]
        
    def findRear(self):
        '''
        Return the rear (last) element of queue
        :param: self: Object
        :rtype: int
        '''
        return self.queue[-1]
    
    def isFull(self):
        '''
        :param: self: Object
        :rtype: bool
        '''
        return len(self.queue) == self.capacity
    
    def isEmpty(self):
        '''
        :param: self: Object
        :rtype: bool
        '''
        return len(self.queue) == 0
        
    def enqueue(self, val):
        '''
        Insert an element to the queue
        :param: self: Object
                val: int, Value to be added to queue
        :rtype: None
        '''
        if self.isFull():
            print('Overflow')
            return
        
        self.queue.append(val)
        print('{} enqueued to queue'.format(val))
    
    def dequeue(self):
        '''
        Remove an element from the queue
        :param: self: Object
        :rtype: None
        '''
        if self.isEmpty():
            print('Underflow')
            return
        
        val = self.queue.pop(0)
        print('{} dequeued from queue'.format(val))

q = Queue(5)
s = [1, 2, 3, 4, 5, 6]

for i in s:
    q.enqueue(i)
print('Queue: {}'.format(q.queue))
q.dequeue()
print('Front: {}'.format(q.findFront()))
print('Rear: {}'.format(q.findRear()))