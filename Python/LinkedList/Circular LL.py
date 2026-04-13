class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new = Node(data)

        if self.head is None:
            new.next = new
            self.head = new
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new
        new.next = self.head
        self.head = new

    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            new.next = new
            self.head = new
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new
        new.next = self.head

    def delete(self, key):
        if self.head is None:
            return

        curr = self.head
        prev = None

        while True:
            if curr.data == key:

                if prev:
                    prev.next = curr.next
                else:
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next

                    temp.next = curr.next
                    self.head = curr.next

                return

            prev = curr
            curr = curr.next

            if curr == self.head:
                print("Value not found")
                return

    def search(self, key):
        if self.head is None:
            return False

        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def display(self):
        if self.head is None:
            print("Empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


cll = CircularLinkedList()

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
        cll.insert_beginning(val)

    elif choice == 2:
        val = int(input("Enter value: "))
        cll.insert_end(val)

    elif choice == 3:
        val = int(input("Enter value to delete: "))
        cll.delete(val)

    elif choice == 4:
        val = int(input("Enter value to search: "))
        print(cll.search(val))

    elif choice == 5:
        cll.display()

    elif choice == 6:
        break

    else:
        print("Invalid choice")