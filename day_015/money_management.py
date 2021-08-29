class Money_Management():
    def remaining_money(self, money, price):
        change = price-money
        if change<0:
            print(f"You paid {abs(change)} extra")
        elif change>=0:
            print(f"${abs(change)} remaining.")
        return change

    def take_money(self, price,item):
        change = price #need exact price
        true_or_false = Money_Management()
        quarters_in_dollar = int(input("How many quarters: "))*0.25
        change = self.remaining_money(quarters_in_dollar, change)
        if change <= 0:
            if change == 0:
                print(f"You have entered sufficient amount\nHere is your {item}\n\n\n\n")
            else:
                print(f"Here is your balance: {abs(change)}\nHere is your {item}\n\n\n\n")
            return True
        dimes_in_dollar = int(input("How many dimes: "))*0.10
        change = self.remaining_money(dimes_in_dollar, change)
        if change <= 0:
            if change == 0:
                print("You have entered sufficient amount")
            else:
                print(f"Here is your balance: {abs(change)}")
            return True
        nickels_in_dollar = int(input("How many nickels: "))*0.05
        change = self.remaining_money(nickels_in_dollar, change)
        if change <= 0:
            if change == 0:
                print("You have entered sufficient amount")
            else:
                print(f"Here is your balance: {abs(change)}")
            return True
        pennies_in_dollar = int(input("How many nickels: "))*0.01
        change = self.remaining_money(pennies_in_dollar, change)
        if change <= 0:
            if change == 0:
                print("You have entered sufficient amount")
            else:
                print(f"Here is your balance: {abs(change)}")
            return True
        else:
            print("There is no sufficient coins")




