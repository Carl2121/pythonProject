

def merch_UI():
    print("Welcome Merchandiser! Here are the products along with their prices\n")
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




dairy = {"Fresh milk": 150, "Butter": 100, "Yogurt":50}
meat = {"Chicken", "Beef", "Pork"}

print(dairy)
print(meat)



def action_dairy():
    pick = input("What do you want to do? (add/remove/change): ").upper()
    if pick == "ADD":
        new_product = input("Enter new product: ")
        dairy.append(new_product)
        print(f"The updated list is {dairy}")

    elif pick == "REMOVE":
        remove_product = input("Enter which product do you want to remove: ").lower()

        if remove_product == "butter":
            del dairy[0]
            print(f"The updated list is {dairy}")

        elif remove_product == "soya":
            del dairy[1]
            print(f"The updated list is {dairy}")

        elif remove_product == "milk":
            del dairy[2]
            print(f"The updated list is {dairy}")

        else:
            print("Invalid input! Type the word of the product you want to remove")


    elif pick == "CHANGE":
        choose_product = input("Enter which product you want to change the price: ").lower()

        if choose_product == "butter":
            change_price = float(input("Enter new price for Butter: "))







def category():
    product = input("ENTER EITHER MEAT OR DAIRY: ").upper()

    if product == "DAIRY":
        action_dairy()

category()