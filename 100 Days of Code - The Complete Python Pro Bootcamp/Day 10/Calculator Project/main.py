import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def operation_selector(operation_choice, num_a, num_b):
    temp = 0
    if operation_choice == "+":
       temp = add(num_a, num_b)

    elif operator_choice == "-":
       temp = subtract(num_a, num_b)

    elif operator_choice == "*":
        temp = multiply(num_a, num_b)

    elif operator_choice =="/":
        temp = divide(num_a, num_b)

    return  temp


print(art.logo)
should_continue = True


while should_continue:

    num_1 = int(input("What's the first number? "))
    operator_choice = input("pick an operator:\n+\n-\n*\n/")
    num_2 = int(input("What's the second number? "))

    output_val = operation_selector(operator_choice, num_1, num_2)

    print(f"{num_1} {operator_choice} {num_2} = {output_val}")

    keep_restart = input(f"Type 'y' to use continue calculating with {output_val}, or 'n' to restart: ")

    if keep_restart == "y":
        num_1 = output_val
        operator_choice = input("pick an operator:\n+\n-\n*\n/")
        num_2 = int(input("What's the second number? "))
        output_val = operation_selector(operator_choice, num_1, num_2)
        print(f"{num_1} {operator_choice} {num_2} = {output_val}")

    elif keep_restart == "n":
        pass

