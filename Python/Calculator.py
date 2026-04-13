def calculatorDisplay():
    
    display = """Welcome to Calculator
    
Choose one operation:
1. Add
2. Subtract
3. Exit
"""
    return(display)


def calculatorFunction(user_choice):
    if user_choice == 1:
        print("Let's perform addition")
        a, b = user_input()
        output = addition(a, b)
        return f"The sum is: {output}"
    elif user_choice == 2:
        print("Let's perform subtraction")
        a, b = user_input()
        output = subtraction(a, b)
        return f"The difference is: {output}"
    else:
        return("Exiting the calculator, bye bye!")

def user_input():
    print("Give two numbers on two lines")
    a = int(input("Number 1 is: "))
    b = int(input("Number 2 is: "))
    return a, b

def addition(a, b):
    return(a + b)

def subtraction(a, b):
    return(a - b)


if __name__ == '__main__':
    while True:
        print(calculatorDisplay())
        user_choice = int(input("Select the operation: "))
        value = calculatorFunction(user_choice)
        print(value)
        # Update your code below this line
        if value == "Exiting the calculator, bye bye!":
            break