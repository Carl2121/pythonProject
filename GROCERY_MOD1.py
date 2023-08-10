# GROCERY_MOD1.py
#This dictionary maps the price of each individual product
PRICES = {
    "Fresh Milk": 150,
    "NAN_Gold(1kg)": 1590,
    "Promil_Gold(1kg)": 1480,
    "GroundBeef": 450,
    "ChickenWings": 280,
    "PorkKnuckles ": 350,
}

#This dictionary insteads maps each products into numbers so the user dont have to type the product name
ITEMS = {
    "1": "Fresh Milk",
    "2": "NAN_Gold(1kg)",
    "3": "Promil_Gold(1kg)",
    "4": "GroundBeef",
    "5": "ChickenWings",
    "6": "PorkKnuckles ",
}

def customer_UI():
    print("Welcome to ABC store! Pick the number of the product you want to buy\n")
    dairy = "Dairy\n1. Fresh Milk: 150\n2. NAN_Gold(1kg): 1590\n3. Promil_Gold(1kg): 1480\n"
    meat = "WetGoods\n4. GroundBeef: 450\n5. ChickenWings: 280\n6. PorkKnuckles : 350"

    print(dairy)
    print(meat)


def customer_pick():
    order = {}
    #Used an empty dictionary named "order" to store the customer's order from the while loop
    #While loop will repeatedly ask the customer if they still want to buy or not
    #If the specific product is already ordered and the user buys it again, it will just accumulate in the "order" dictionary

    while True:
        item_num = input("Enter the item number you want to buy: ")
        item = ITEMS.get(item_num)
        if item is None:
            print("Invalid item number. Please try again.")
            continue
        quantity = int(input("Enter the quantity you want to buy: "))

        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity

        another_item = input("Do you want to add another item? (y/n): ").upper()
        if another_item == "N":
            break

    return order


def get_price(item):
    return PRICES[item]

#This function above takes an item name as input and returns the price of that item from the PRICES dictionary: