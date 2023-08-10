from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": sub, "*": mul, "/": divide}


def calculator():
    restart = True

    num1 = int(input("What is the first number?: "))

    for symbols in operations:
        print(symbols)

    while restart:
        operations_symbols = input("Pick an operation: ")
        num2 = int(input("What is the next number?: "))
        calculator_function = operations[operations_symbols]
        answer = calculator_function(num1, num2)
        print(f"{num1} {operations_symbols} {num2} = {answer}")

        cal_continue = input(
            f"Type 'y' to continue calculating with {answer} or type 'n' to exit.: "
        )

        if cal_continue == "y":
            num1 = answer
        else:
            restart = False
            calculator()


calculator()
