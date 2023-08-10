#GROCERY_MOD2.py

PRICES = {
    "FRESH MILK": 150,
    "NAN_GOLD(1KG)": 1590,
    "PROMIL_GOLD(1KG)": 1480,
    "GROUNDBEEF": 450,
    "CHICKENWINGS": 280,
    "PORKKUNCKLES ": 350,
}


def merch_UI():
    print("Welcome Merchandiser! Here are the products along with their prices\n")
    dairy = "Dairy\n1. Fresh Milk: 150\n2. NAN_Gold(1kg): 1590\n3. Promil_Gold(1kg): 1480\n"
    meat = "WetGoods\n4. GroundBeef: 450\n5. ChickenWings: 280\n6. PorkKnuckles : 350"


    print(dairy)
    print(meat)

#One function for dairy products
def action_dairy(prices):
    pick = input("What do you want to do? (add/remove/edit): ").upper()
    if pick == "ADD":
        new_product = input("Enter new product: ")
        new_price = float(input("Enter price for the new product: "))
        prices[new_product] = new_price
        print(f"The updated list is: {prices}")

    elif pick == "REMOVE":
        print("Enter the full name of the product please!")
        remove_product = input("Enter which product do you want to remove: ").upper()

        if remove_product in prices:
            del prices[remove_product]
            print(f"The updated list is: {prices}")
        else:
            print("Invalid input! Type the word of the product you want to remove")


    elif pick == "EDIT":
        print("Enter the full name of the product please!")
        choose_product = input("Enter which product you want to change the price: ").upper()

        if choose_product in prices:
            change_price = float(input(f"Enter new price for {choose_product.capitalize()}: "))
            prices[choose_product] = change_price
            print(f"The updated list is: {prices}")
        else:
            print("Invalid input! Type the word of the product you want to change the price")

#One function for WetGoods
def action_meat(prices):
    pick = input("What do you want to do? (add/remove/edit): ").upper()
    if pick == "ADD":
        new_product = input("Enter new product: ")
        new_price = float(input("Enter price for the new product: "))
        prices[new_product] = new_price
        print(f"The updated list is: {prices}")

    elif pick == "REMOVE":
        print("Enter the full name of the product please!")
        remove_product = input("Enter which product do you want to remove: ").upper()

        if remove_product in prices:
            del prices[remove_product]
            print(f"The updated list is: {prices}")
        else:
            print("Invalid input! Type the word of the product you want to remove")


    elif pick == "EDIT":
        print("Enter the full name of the product please!")
        choose_product = input("Enter which product you want to change the price: ").upper()

        if choose_product in prices:
            change_price = float(input(f"Enter new price for {choose_product.capitalize()}: "))
            prices[choose_product] = change_price
            print(f"The updated list is: {prices}")
        else:
            print("Invalid input! Type the word of the product you want to change the price")


def category():
    print("\n")
    product = input("ENTER EITHER WETGOODS OR DAIRY: ").upper()

    if product == "DAIRY":
        action_dairy(PRICES)
    elif product == "WETGOODS":
        action_meat(PRICES)
    else:
        print("Invalid input! Type either 'wetgoods' or 'dairy'")


