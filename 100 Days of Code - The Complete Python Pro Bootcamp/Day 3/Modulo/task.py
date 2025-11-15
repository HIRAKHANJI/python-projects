num_input = int(input("Enter a number to check EVEN or ODD: "))

modulo_value = (num_input % 2)

if modulo_value == 0:
    print("EVEN")
else:
    print("ODD")