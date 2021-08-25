def number_check(input_number, generated_number,chances,tries):
    """This function checks whether the number guessed by user is above, equal or below the other random number
    where both the numbers are given as input"""
    if input_number == generated_number:
        print(f"You guessed it correct. The number is {input_number}")
        return "y"
    elif input_number > generated_number:
        print(f"{input_number} is too high\nYou got {chances - tries - 1} tries left")
    else:
        print(f"{input_number} is too low\nYou got {chances - tries - 1} tries left")