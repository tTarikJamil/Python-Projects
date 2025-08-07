from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
# result = operation["*"]
# print(result(3,5))
def calculator():
    print(logo)
    first = float(input("What's the first number?: "))
    running = True
    while running:
        for symbol in operation:
            print(symbol)
        operator = input("Pick an operation: ")
        second = float(input("What's the next number?: "))
        answer = operation[operator](first, second)
        print(f"{first}{operator}{second} = {answer}")
        again_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if again_calculation == "y":
            first = answer
        elif again_calculation == "n":
            running = False
            print("\n" * 20)
            calculator()
calculator()
