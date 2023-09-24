# def format_name(name, surname):
#     """The function formats the name and surname, so that they'll start with a capital letter"""    
#     f_name = name.title()
#     l_name = surname.title()        
#     return f_name + " " + l_name

# print(format_name("noemi", "pintaldi"))

import art
from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    continue_operations = True
    for operation in operations:
        print(operation)

    while continue_operations == True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
                
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        
        if response == "y":
            num1 = answer
            continue_operations = True
        elif response == "n":
            continue_operations = False
            calculator()
            
calculator()