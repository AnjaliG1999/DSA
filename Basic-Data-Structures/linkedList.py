#!usr/bin/env python3

# List element instance
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node

# Create a linkedList instance
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        node = Node(data)
        if not self.get_head():
            self.__head = node
        else:
            nxt = self.get_tail()
            nxt.set_next(node)
        
        self.__tail = node
        
    def display(self):
        temp = self.get_head()
        while temp:
            print(temp.get_data(), end=" ")
            temp = temp.get_next()

list1=LinkedList()
# add new elements to the list
count = int(input('Enter total items to be added: '))
print('Add items:')
for c in range(count):
    list1.add(input())
    
print("Linkedlist data(Head to Tail): ", end="")
list1.display()
