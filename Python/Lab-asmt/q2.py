# Node class
class Node:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []


# Queue implementation (no collections)
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


# BFS search
def bfs_search(root, target):
    q = Queue()
    q.enqueue((root, root.name))

    while not q.is_empty():
        node, path = q.dequeue()

        if node.name == target:
            print("File found at path:", path)
            return

        for child in node.children:
            q.enqueue((child, path + "/" + child.name))

    print("File not found")


# Creating sample hierarchy
root = Node("root")
folder1 = Node("folder1")
folder2 = Node("folder2")
file1 = Node("file1.txt", True)
file2 = Node("file2.txt", True)

root.children.append(folder1)
root.children.append(folder2)
folder1.children.append(file1)
folder2.children.append(file2)

# Search
bfs_search(root, "file2.txt")