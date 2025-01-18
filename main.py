from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    should_continue = True
    first_number = int(input("Enter the first number, please: "))

    while should_continue:
        mathematical_operator = input("Type a mathematical operator, a choice of '+', '-', '*', '/': ")

        while mathematical_operator not in operations:
            mathematical_operator = input("please enter: '+', '-', '*' or '/' : ")

        second_number = int(input("Enter the second number, please: "))

        for operator in operations:
            if mathematical_operator == operator:
                result = operations[operator](first_number, second_number)
                print(f"{first_number} {operator} {second_number} = {result}")

        decision = input(
            "Do you want to continue working with the previous result: type 'y' for 'yes' and 'n' for 'no' : ").lower()

        if decision == 'y':
            first_number = result
        elif decision == 'n':
            should_continue = False
            print("\n" *25)
            calculator()
        else:
            print("enter 'y' or 'n': ")

calculator()