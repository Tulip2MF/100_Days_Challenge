from data_higher_lower import data
from art_higher_lower import logo, vs
from random import choice
from functions_higher_lower import check_followers

updated_data = data
a_card = choice(list(updated_data))
updated_data.remove(a_card)
should_continue = True
print(logo)
score = 0

while should_continue:

    b_card = choice(list(updated_data))
    updated_data.remove(b_card)

    print(f"Compare A: {a_card['name']}, {a_card['description']} from {a_card['country']}\n"
          f"{vs}\n"
          f"Compare B: {b_card['name']}, {b_card['description']} from {b_card['country']}")

    user_input = input("Who has more followers? Type 'A' or 'B'").lower()
    if user_input == 'a':
        should_continue = check_followers(a_card['name'], a_card['name'], a_card['follower_count'], b_card['name'],
                                          b_card['follower_count'])

    elif user_input == 'b':
        should_continue = check_followers(b_card['name'], a_card['name'], a_card['follower_count'], b_card['name'],
                                          b_card['follower_count'])
    a_card = b_card
    score += 1
    print(f"Current Score: {score}")
