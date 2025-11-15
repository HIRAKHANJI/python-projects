
age = 0
try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please enter only numerical responses.")

if age > 18:
    print(f"You can drive at age {age}.")
