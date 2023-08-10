# GROCERY.py

import GROCERY_MOD1
import GROCERY_MOD2

id = int(input("Enter user ID: "))
username = input('Enter username: ')
print(f"Welcome {username} with ID number: {id}")
print("\n")

welcome = int(input("Pick 1 if Customer | Pick 0 if Merchandiser\nEnter number: "))

if welcome == 1:
    GROCERY_MOD1.customer_UI()
    print("\n")
    order = GROCERY_MOD1.customer_pick()

    total_cost = 0
    print("Your order:")
    for item, quantity in order.items():
        price = GROCERY_MOD1.get_price(item)
        cost = price * quantity
        print(f"{quantity} x {item} @ {price} = {cost}")
        total_cost += cost
    print(f"Total cost: {total_cost}")

elif welcome == 0:
    GROCERY_MOD2.merch_UI()
    GROCERY_MOD2.category()

else:
    print("Wrong Input Choose only either 1 or 2! ")



"""
elif welcome == 2:
    GROCERY_MOD2.merch_UI()
    print("\n")
    category = input("Enter category (dairy/meats): ")
    action = input("Enter action (add/remove/change): ")

    if action == "add" or action == "change":
        product_name = input("Enter product name: ").capitalize()
        new_price = float(input("Enter new price: "))
    else:
        product_name = input("Enter product name: ").capitalize()
        new_price = None

    GROCERY_MOD2.modify_products(category, action, product_name, new_price)

"""


