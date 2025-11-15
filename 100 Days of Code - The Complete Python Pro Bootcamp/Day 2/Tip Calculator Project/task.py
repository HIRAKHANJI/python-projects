print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give?\n10% | 12% | 15%: "))
people = int(input("How many people to split the bill? "))

tip_added_bill_amount = bill + (bill * (tip / 100))
per_person_amount = round((tip_added_bill_amount / people), 2)

print(f"Each person should pay: ${per_person_amount}")

