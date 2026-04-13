class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class BrowserHistory:
    def __init__(self):
        self.top = None

    def visit(self, page):
        new_node = Node(page)
        new_node.next = self.top
        self.top = new_node

    def back(self):
        if self.top is None:
            print("No history")
            return

        temp = self.top
        self.top = temp.next

    def current_page(self):
        if self.top:
            print("Current page:", self.top.data)
        else:
            print("No page")

    def display(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next


b = BrowserHistory()

b.visit("google.com")
b.visit("github.com")
b.visit("stackoverflow.com")

b.display()

b.back()
b.current_page()