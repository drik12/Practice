# Circular Linked List with Insertion, Deletion, and Traversal
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class CircularLinkedList:
    def __init__(self):
        self.tail = None  # tail.next points to head
 
    def insert_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            self.tail.next = self.tail  # points to itself
        else:
            new_node.next = self.tail.next  # new_node -> head
            self.tail.next = new_node       # old tail -> new_node
            self.tail = new_node            # update tail
 
    def delete(self, data):
        if self.tail is None:
            print("List is empty.")
            return
 
        head = self.tail.next
        # Only one node
        if self.tail == head and head.data == data:
            self.tail = None
            print(f"Deleted {data}")
            return
 
        # Traverse to find the node before target
        prev = self.tail
        curr = head
        while True:
            if curr.data == data:
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                print(f"Deleted {data}")
                return
            prev = curr
            curr = curr.next
            if curr == head:
                break
 
        print(f"{data} not found in list.")
 
    def traverse(self):
        if self.tail is None:
            print("List is empty.")
            return
        head = self.tail.next
        curr = head
        result = []
        while True:
            result.append(str(curr.data))
            curr = curr.next
            if curr == head:
                break
        print("List:", " -> ".join(result) + " -> (back to head)")
 
 
# Main
cll = CircularLinkedList()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)
cll.insert_end(40)
 
print("After inserting 10, 20, 30, 40:")
cll.traverse()
 
cll.delete(20)
print("After deleting 20:")
cll.traverse()
 
cll.delete(99)