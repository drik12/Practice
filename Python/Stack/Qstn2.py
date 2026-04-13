def check_balanced(expression):
    stack = []

    for char in expression:
        if char == "(":
            stack.append(char)

        elif char == ")":
            if not stack:
                return "Not Balanced"
            stack.pop()

    if len(stack) == 0:
        return "Balanced"
    else:
        return "Not Balanced"


expression = "(8 + 2) * 5"
print(check_balanced(expression))