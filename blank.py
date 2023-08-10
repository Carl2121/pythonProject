



def customer_UI():
    print("Welcome to ABC store! Pick the number of the product you want to buy\n")
    dairy = "Dairy\n1. Fresh Milk: 150\n2. Butter: 100\n3. Yogurt: 50\n"
    meat = "Meat\n4. Chicken: 200\n5. Beef: 300\n6. Pork: 250"

    print(dairy)
    print(meat)



PRICES = {
    "Fresh Milk": 150,
    "Butter": 100,
    "Yogurt": 50,
    "Chicken": 200,
    "Beef": 300,
    "Pork": 250,

}

ITEMS = {
    "1": "Fresh MilK",
    "2": "Butter",
    "3": "Yogurt",
    "4": "Chicken",
    "5": "Beef",
    "6": "Pork",

}




def customer_pick():

    order = {}

    while True:
        item_num = input("Enter item number you want to buy: ")
        item = ITEMS.get(item_num)
        quantity = int(input("Enter quantity: "))

        if item is None:
            print("Invalid Input")

        if item in order:
            order[item] += quantity

        else:
            order[item] = quantity

        another_item = input("Would you like to buy again? [y/n]: ").upper()
        if another_item == "N":
            break

    return order




def get_prices(item):
    return PRICES[item]



