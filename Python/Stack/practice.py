class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return
        
        temp = self.top
        self.top = temp.next
        return temp.data
    
    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None
        return self.top.data
    
    def display(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next