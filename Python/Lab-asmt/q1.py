# Stack implementation using list
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


# Priority function
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


# Infix to Postfix conversion
def infix_to_postfix(expr):
    stack = Stack()
    output = []

    for ch in expr:
        if ch.isalnum():
            output.append(ch)

        elif ch == '(':
            stack.push(ch)

        elif ch == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()

        else:
            while (not stack.is_empty() and 
                   precedence(stack.peek()) >= precedence(ch)):
                output.append(stack.pop())
            stack.push(ch)

    while not stack.is_empty():
        output.append(stack.pop())

    return "".join(output)


# Example
expr = "A+B*(C-D)"
print("Postfix:", infix_to_postfix(expr))