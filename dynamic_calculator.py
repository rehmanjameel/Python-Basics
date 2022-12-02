from calc_art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
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
    num1 = float(input("Enter first number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbols = input("Pick an operation: ")
        num2 = float(input("Enter next number: "))
        calculation_function = operations[operation_symbols]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbols} {num2} = {answer}")

        get_permission = input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculation.: ")

        if get_permission == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
