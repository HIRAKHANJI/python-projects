import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]



player_choice = int(input("Choose rock|paper|scissors: "))

computer_choice = random.randint(0, 2)

if player_choice == computer_choice:
    print(options[player_choice])
    print("Computer Choice" + options[computer_choice])
    print("draw")

elif player_choice == 1 and computer_choice == 0:
    print(options[player_choice])
    print("Computer Choice" + options[computer_choice])
    print("You Win!")

elif player_choice == 2 and computer_choice == 1:
    print(options[player_choice])
    print("Computer Choice" + options[computer_choice])
    print("You Win!")

elif player_choice == 0 and computer_choice == 2:
    print(options[player_choice])
    print("Computer Choice" + options[computer_choice])
    print("You Win!")

else:
    print(options[player_choice])
    print("Computer Choice" + options[computer_choice])
    print("You Lose!")

