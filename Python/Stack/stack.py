class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top   # corrected line
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

    def search(self, key):
        temp = self.top
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Top:", s.peek())

s.pop()
s.display()

print(s.search(20))
print(s.search(100))