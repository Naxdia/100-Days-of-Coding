 Day-10---Calculator
#Day 10 - Calculator Project

#Defining functions for each operation
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }
### operations["*"] is equivalent to the word 'multiply' which calls that function
#print(operations["*"](4,8))




def calculator():
    num1 = float(input("What is the first number?: "))
    should_continue = True
    #For loop to iterate through the dictionary and print the keys for the user to see what operations are available
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is the second number?: "))
        result = (operations[operation_symbol](num1, num2))
        #Displaying the entire equation to the user
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or 'exit' to leave the program: ")
        if choice == "y":
            num1 = result
        elif choice == "n":
            print("\n"*20)
            #Recursive call to restart the calculator function
            calculator()
        else:
            choice == "exit"
            return
              
        
calculator()

