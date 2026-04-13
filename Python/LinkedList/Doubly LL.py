class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def insert_beginning(self, data):
        new = Node(data)

        if self.head is not None:
            self.head.prev = new
            new.next = self.head

        self.head = new


    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new
        new.prev = temp


    def delete(self, key):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev is None:  
            self.head = temp.next
            if self.head:
                self.head.prev = None
        else:
            temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev


    def search(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False


    def display(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


    def traverse_forward(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


    def traverse_backward(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


dll = DoublyLinkedList()


while True:
    print("\nMENU")
    print("1 Insert at Beginning")
    print("2 Insert at End")
    print("3 Delete")
    print("4 Search")
    print("5 Display")
    print("6 Traverse Forward")
    print("7 Traverse Backward")
    print("8 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        dll.insert_beginning(val)

    elif choice == 2:
        val = int(input("Enter value: "))
        dll.insert_end(val)

    elif choice == 3:
        val = int(input("Enter value to delete: "))
        dll.delete(val)

    elif choice == 4:
        val = int(input("Enter value to search: "))
        print(dll.search(val))

    elif choice == 5:
        dll.display()

    elif choice == 6:
        dll.traverse_forward()

    elif choice == 7:
        dll.traverse_backward()

    elif choice == 8:
        print("Exiting...")
        break

    else:
        print("Invalid choice")