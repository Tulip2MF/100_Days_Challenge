from art_gavel import logo

print(logo, "\n\n Welcome to the secret auction program")
database_dictionary = {}
name_list = []
bid_list = []
highest_bid = 0
highest_bidder = ""

while True:
    user_name = input("What is your name? ")
    user_bid = int(input("What is your bid? $"))
    database_dictionary[user_name] = user_bid
    continue_bid = input("Are there any other bidders? Press 'Y' for yes and 'N' for No").lower()
    if continue_bid == 'y':
        print("\n" * 10)

    elif continue_bid == 'n':
        for user in database_dictionary:
            bid_amount = database_dictionary[user]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                highest_bidder = user
        break
print(f"The item goes to {highest_bidder} for {highest_bid}")
