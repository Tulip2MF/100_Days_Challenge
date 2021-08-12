print("Welcome to treasure island.\nYour mission is to find the treasure")
direction=input('''You're at a cross road. where do you want to go? Type "left" or "right"''').lower()




if direction == "left":
    travel = input('''You reached a lake. Would you like to wait or swim?''').lower()
    if travel == "wait":
        door = input('''You reached a castle. Which door to select?\nRed, Blue or Yellow?''').lower()
        if door == "yellow":
            print("You Win. Congratulations")
        elif door=="red" or "blue":
            print("Game Over")
        else:
            print("Enter Correct Input")
    elif travel=="swim":
        print("Game Over")
    else:
        print("Enter Correct Input")
elif direction =="right":
    print("Gate Over")
else:
    print ("Enter Correct Input")
