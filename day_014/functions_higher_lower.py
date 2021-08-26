
def check_followers(user_selection, a_name,a_follower_count,b_name,b_follower_count):
    """ This function will check the user selection against the first and second cards and give result"""
    if a_follower_count == b_follower_count:
        print("Both of them got same number of followers")
    elif a_follower_count > b_follower_count:
        if user_selection == a_name:
            print("You are correct")
            user_won = True
        else:
            print("Sorry!")
            user_won = False
        print(f"{a_name} got {a_follower_count-b_follower_count} more followers than {b_name}")
    else:
        if user_selection == b_name:
            print("You are correct")
            user_won = True
        else:
            print("Sorry!")
            user_won = False
        print(f"{b_name} got {b_follower_count-a_follower_count} more followers than {a_name}")
    return user_won