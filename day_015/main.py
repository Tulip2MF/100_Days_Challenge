from user_input import user_input
from store_room import Resources
from coffee_machine import Coffee_Machine
from money_management import Money_Management
#coffee_details = user_input()
stock = Resources
coffeeMachine = Coffee_Machine()
moneyManagement = Money_Management()
while 1:

    coffee_details = user_input()
    if coffee_details == "off":
        break
    elif coffee_details == "report":
        print(stock)

    elif coffee_details["cost"]>0:
        if coffeeMachine.is_resource_sufficient(coffee_details["ingredients"],stock) == "yes":
            moneyManagement.take_money(coffee_details["cost"],coffee_details['item'])
            stock = coffeeMachine.Stock_Taking(coffee_details["ingredients"],stock)
        if stock['water']>=50 and stock['coffee']>=18:
            print("You can have\n * Espresso")
            if stock['water']>=200 and stock['milk']>=150 and stock['coffee']>=24:
                print("* latte")
            if stock['water']>=250 and stock['milk']>=100 and stock['coffee']>=24:
                print("* Cuppuccino")
        else:
            print(f"Please refill\nHave following\n{stock}")
    else:
        print("Enter correctly")




