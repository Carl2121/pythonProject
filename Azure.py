#add elements on a list
def addingredient():
    topping = ["peperoni", "cheese", "mozzarella", "mushrooms", "pineapple"]

    topping1 = []

    while True:
        userinput = input("Enter the topping you want to add type [done] if you are finish: ").lower()
        if userinput == "done":
            break
        elif userinput in topping1 or userinput in topping:
            print("topping is already in the list!")
        else:
            topping1.append(userinput)

    topping.extend(topping1)
    print(topping)



#edit that bich lesgooo
PRICES = {"Fresh Milk": 150, "NAN_Gold(1kg)": 1590, "Promil_Gold(1kg)": 1480, "GroundBeef": 450, "ChickenWings": 280,"PorkKnuckles": 350}

def edit():
    pick = input("What do you want to do? (add/remove/edit): ").lower()
    if pick == "add":
        new_item = input("Enter new item: ")
        new_price = float(input("Enter new product price: "))
        PRICES[new_item] = new_price
        print(f"the new list is {PRICES}")

    elif pick == "remove":
        print(PRICES)
        remove = input("Enter the product you want to remove: ")
        if remove in PRICES:
            del PRICES[remove]
            print(f"the new list is {PRICES}")

        else:
            print("Invalid Input! Try putting the products inside the list!")

    elif pick == "edit":
        print(PRICES)
        edits = input("Enter the product you want to edit: ")
        if edits in PRICES:
            edits_price = float(input(f"Enter new price for {edits}: "))
            PRICES[edits] = edits_price
            print(f"the new list is {PRICES}")
        else:
            print("Invalid input! Type the word of the product you want to change!")



