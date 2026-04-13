class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        
        temp = self.front
        data = temp.data
        self.front = temp.next

        if self.front is None:
            self.rear = None
        
        return data

    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return None
        return self.front.data

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def search(self, key):
        temp = self.front
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        count = 0
        temp = self.front
        while temp:
            count += 1
            temp = temp.next
        return count


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
# Output: 10 -> 20 -> 30 -> None

print(q.peek())   # 10

q.dequeue()
q.display()
# Output: 20 -> 30 -> None

print(q.search(30))   # True
print(q.search(100))  # False