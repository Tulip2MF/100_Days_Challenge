class Coffee_Machine:
    def Stock_Taking(self, ingredients, stock):
        # from numpy import subtract
        from collections import Counter
        remaining_stock = {'water':(stock['water']-ingredients['water']),'milk':(stock['milk']-ingredients['milk']),'coffee':(stock['coffee']-ingredients['coffee'])}

        # selected_item = Counter(ingredients)
        # current_stock = Counter(stock)
        # # remaining_stock = subtract(current_stock, selected_item)
        # remaining_stock = current_stock - selected_item  # chances of error
        return remaining_stock

    # def report(self, ingredients, stock):
    #     remaining_resource = self.Stock_Taking(ingredients, stock)
    #     print(remaining_resource)
    #     print(remaining_resource)

    def is_resource_sufficient(self, ingredients, stock):
        remaining_resource = self.Stock_Taking(ingredients, stock)
        water = remaining_resource["water"]
        milk = remaining_resource["milk"]
        coffee = remaining_resource["coffee"]
        if water >= 0 and milk >= 0 and coffee >= 0:
            return "yes"
        else:
            print("Not enough ingredients")
