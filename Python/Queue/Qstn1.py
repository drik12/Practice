class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PrinterQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, job):
        new_node = Node(job)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("No jobs in queue")
            return

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        print("Printing:", temp.data)

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


p = PrinterQueue()

p.enqueue("Doc1")
p.enqueue("Doc2")
p.enqueue("Doc3")

p.display()

p.dequeue()

p.display()