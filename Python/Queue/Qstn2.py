class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TicketQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, ticket):
        new_node = Node(ticket)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("No tickets available")
            return

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        print("Serving ticket:", temp.data)

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


t = TicketQueue()

t.enqueue("T101")
t.enqueue("T102")
t.enqueue("T103")

t.display()

t.dequeue()

t.display()