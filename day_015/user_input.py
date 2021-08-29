def user_input():
    from store_room import MENU
    from coffee_machine import Coffee_Machine

    input_prompt = input("What would you like? Press the corresponding number\n1.Espresso\n2.Latte\n3.Cappuccino: ")

    if input_prompt == "1":
        return {'ingredients': MENU["espresso"]["ingredients"], 'cost': MENU["espresso"]["cost"],'item':"espresso"}
    elif input_prompt == "2":
        return {'ingredients': MENU["latte"]["ingredients"], 'cost': MENU["latte"]["cost"],'item':"latte"}
    elif input_prompt == "3":
        return {'ingredients': MENU["cappuccino"]["ingredients"], 'cost': MENU["cappuccino"]["cost"],'item':"cappuccino"}
    elif input_prompt == "report":
        return "report"
    elif input_prompt == "off":

        return "off"
    else:
        print("Enter correct parameter!")
