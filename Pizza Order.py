print("Welcome to Python pizza deliveries!")
pizzaSize = input("What pizza size you want? Press: \n S for Small\n M for Medium\n L for Large\n")
addPepperoni = input("Do you want pepperoni? Press\nY for Yes \nN for No\n")
addCheese = input("Do you want extra cheese? Press\nY for Yes \nN for No\n")

smallPizzaPrice = 15
mediumPizzaPrice = 20
largePizzaPrice = 25
smallPepperoni = 2
mediumLargePepperoni = 3
extraCheese = 1
bill = 0


if pizzaSize == 'L':
    bill = largePizzaPrice
    if addPepperoni == 'Y':
        bill = bill+mediumLargePepperoni
elif pizzaSize == 'M':
    bill = mediumPizzaPrice
    if addPepperoni == 'Y':
        bill = bill + mediumLargePepperoni

elif pizzaSize == 'S':
    bill = smallPizzaPrice
    if addPepperoni == 'Y':
        bill = bill + smallPepperoni

if addCheese == "Y":
    bill += 1

print("Total bill is: ", bill)
