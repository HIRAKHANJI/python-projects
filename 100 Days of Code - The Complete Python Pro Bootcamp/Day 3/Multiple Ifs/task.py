print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Children pay $5.")
        bill = 5
    elif age <= 18:
        print("Teens pay $7.")
        bill = 7
    else:
        print("Adults pay $12.")
        bill = 12

    photo_confirmation = input("Do you want a photo for an additional $3? (y/n): ")
    if photo_confirmation == "y":
        print(f"Your payable amount now is: ${bill + 3}")
    else:
        print(f"your payable amount now is: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
