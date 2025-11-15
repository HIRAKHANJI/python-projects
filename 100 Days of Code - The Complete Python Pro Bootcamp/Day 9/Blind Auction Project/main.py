import art
print(art.logo)

# TODO-1: Ask the user for input

def compare_bids(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount_temp = bidding_dictionary[bidder]
        if highest_bid < bid_amount_temp:
            highest_bid = bid_amount_temp
            winner = bidder

    print(f"The winner is {winner}, with an amount of ${highest_bid}")

Bid_ledger = {}
continue_or_no = True

while continue_or_no:
    user_name = input("Name: ")
    bid_amount = int(input("Bid amount: "))
    Bid_ledger[user_name] = bid_amount
    add_more_users = input("Add another bidder (y/n): ")

    if add_more_users == "n":
        continue_or_no = False
        compare_bids(Bid_ledger)
    elif add_more_users == "y":
        print("\n" * 20)




# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


