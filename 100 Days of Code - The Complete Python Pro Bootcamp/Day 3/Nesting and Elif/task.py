print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How Old are you?"))

if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        print("Ticket Price: $5")
    elif age <= 18:
        print("Ticket Price: $7")
    elif age > 18:
        print("Ticket Price: $12")

else:
    print("Sorry you have to grow taller before you can ride.")
