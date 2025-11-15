import art
import random
print(art.logo)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_cards(cards):
    """Take a list of cards and calculate the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has a black jack"
    elif u_score == 0:
        return "Win with a black jack"
    elif u_score > 21:
        return "You went over 21, you lose"
    elif c_score > 21:
        return "Opponent went over 21, you win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"


user_cards = []
computer_cards = []
is_gave_over = False
computer_score = -1
user_score = -1

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
while not is_gave_over:
    user_score = calculate_cards(user_cards)
    computer_score = calculate_cards(computer_cards)
    print(f"Your cards: {user_cards}. Current score: {user_score}")
    print(f"Computer cards: {computer_cards}. Current score: {computer_score}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True

    else:
        user_should_deal = input("Type 'y' to get another card and 'n' to pass:  ")

        if user_should_deal == "y":
            user_cards.append(deal_card())

        else:
            is_gave_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_cards(computer_cards)

print(compare_scores(user_score, computer_score))