import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter_hold = []
symbol_hold = []
number_hold = []
final_hold = []
password = ""

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_characters = nr_letters + nr_numbers + nr_symbols


for hold_l in range(0, nr_letters):

    current = random.choice(letters)
    letter_hold.append(current)


for hold_s in range(0, nr_symbols):

    current = random.choice(symbols)
    symbol_hold.append(current)


for hold_n in range(0, nr_numbers):

    current = random.choice(numbers)
    number_hold.append(current)


for final_loop in range(0, total_characters):
    final_hold = letter_hold + symbol_hold + number_hold
    random.shuffle(final_hold)
    password = ''.join(final_hold)

print(f"Your password: {password}")


