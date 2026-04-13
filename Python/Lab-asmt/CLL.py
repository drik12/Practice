class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Delete node
    def delete(self, key):
        if self.head is None:
            return

        curr = self.head
        prev = None

        while True:
            if curr.data == key:
                if prev is not None:
                    prev.next = curr.next
                else:
                    # deleting head
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    self.head = curr.next
                    temp.next = self.head
                return

            prev = curr
            curr = curr.next

            if curr == self.head:
                break

    # Traverse
    def traverse(self):
        if self.head is None:
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")


# Example
cll = CircularLinkedList()
cll.insert(10)
cll.insert(20)
cll.insert(30)

print("List:")
cll.traverse()

cll.delete(20)

print("After deletion:")
cll.traverse()