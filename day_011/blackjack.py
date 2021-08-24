import random


def blackjack():
    from random import choice

    original_cards = {'A': 11, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'K': 10, 'Q': 10}
    cards = {'A': 11, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'K': 10, 'Q': 10}

    player_first_card = choice(list(cards.keys()))
    cards.pop(player_first_card)
    player_second_card = choice(list(cards.keys()))
    cards.pop(player_second_card)
    dealer_first_card = choice(list(cards.keys()))
    cards.pop(dealer_first_card)
    dealer_second_card = choice(list(cards.keys()))
    cards.pop(dealer_second_card)
    print(f"Player got {player_first_card}")
    player_total_points = original_cards[player_first_card] + original_cards[player_second_card]
    dealer_total_points = original_cards[dealer_first_card] + original_cards[dealer_second_card]
    player_cards = 2
    dealer_cards = 2
    dealer_third_card = ""
    player_third_card = ""

    print(f"Player got {player_first_card} & {player_second_card}")
    print(f"Dealer got {dealer_first_card}")

    should_continue = input("Do you want to continue? Type Yes or No").lower()
    if dealer_total_points < 17:
        dealer_third_card = choice(list(cards.keys()))
        cards.pop(dealer_third_card)
        dealer_total_points += original_cards[dealer_third_card]
        dealer_cards += 1
    if should_continue == "no":
        pass
    elif should_continue == "yes":
        player_third_card = choice(list(cards.keys()))
        cards.pop(player_third_card)
        player_cards += 1

        print(f"Player got {player_first_card} ,{player_second_card} & {player_third_card}")
        player_total_points += original_cards[player_third_card]

    if dealer_total_points > 21 or player_total_points > 21:
        if dealer_first_card == 'A' or dealer_second_card == 'A' or dealer_third_card == 'A':
            dealer_total_points-=10
        elif player_first_card == 'A' or player_second_card == 'A' or player_third_card == 'A':
            player_total_points-=10
        if dealer_total_points > 21:
            print("Player Wins")

        else:
            print("Dealer Wins")
    else:
        if dealer_total_points > player_total_points:
            print("Dealer Wins")
        else:
            print("Player Wins")

    if player_cards == 2:
        print(f"Player got cards: {player_first_card}, {player_second_card}")

    elif player_cards == 3:
        print(f"Player got cards: {player_first_card}, {player_second_card}, {player_third_card}")
    if dealer_cards == 2:
        print(f"Dealer got cards: {dealer_first_card}, {dealer_second_card}")
    elif dealer_cards == 3:
        print(f"Dealer got cards: {dealer_first_card}, {dealer_second_card}, {dealer_third_card}")
    if input("Would you like to play again? Press 'Y' if Yes").lower() == 'y':
        blackjack()
    else:
        print("Have a great day")
blackjack()