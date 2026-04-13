class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new = Node(data)
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

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()

while True:
    print("\nMENU")
    print("1.Insert Beginning")
    print("2.Insert End")
    print("3.Delete")
    print("4.Search")
    print("5.Display")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        ll.insert_beginning(val)

    elif choice == 2:
        val = int(input("Enter value: "))
        ll.insert_end(val)

    elif choice == 3:
        val = int(input("Enter value to delete: "))
        ll.delete(val)

    elif choice == 4:
        val = int(input("Enter value to search: "))
        print(ll.search(val))

    elif choice == 5:
        ll.display()

    elif choice == 6:
        break

    else:
        print("Invalid choice")