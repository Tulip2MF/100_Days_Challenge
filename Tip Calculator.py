print("Welcome to the tip calculator")
initialBill =int(input("What was the total bill?\n"))
peopleCount =int(input("How many people to split the bill?\n"))
tipPercentage = float(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
billAfterTip= initialBill*(1+ (tipPercentage/100))
contribution= billAfterTip/peopleCount
contribution= round(contribution,4)
print(f"Each person would pay: {contribution}")
