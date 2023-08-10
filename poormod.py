from GROCERY_MOD1 import get_price


def merch_UI():
    print("Welcome Merchandiser! Here are the products along with their prices\n")
    dairy = "Dairy\n1. Fresh Milk: 150\n2. Butter: 100\n3. Yogurt: 50\n"
    meat = "Meat\n4. Chicken: 200\n5. Beef: 300\n6. Pork: 250"

    print(dairy)
    print(meat)





def modify_products(category, action, product_name=None, new_price=None):
    """
    Modifies the names and prices of products in a grocery store.

    Parameters:
    category (str): Either "dairy" or "meats".
    action (str): The action to perform: "add", "remove", or "change".
    product_name (str): The name of the product to modify. Required for "change" and "remove" actions, but not for "add".
    new_price (float): The new price of the product. Required for "add" and "change" actions, but not for "remove".

    Returns:
    None
    """
    # Define the list of products for each category
    dairy_products = ["Fresh Milk", "Butter", "Yogurt"]
    meat_products = ["Chicken", "Beef", "Pork"]

    # Check that the category is valid
    if category.lower() not in ["dairy", "meats"]:
        print("Invalid category. Please choose either 'dairy' or 'meats'.")
        return

    # Perform the requested action
    if action.lower() == "add":
        # Check that the product name is not already in the list
        if product_name in dairy_products or product_name in meat_products:
            print("Product already exists.")
            return
        # Add the new product to the appropriate list
        if category.lower() == "dairy":
            dairy_products.append(product_name)
        else:
            meat_products.append(product_name)
        # Set the price for the new product
        if new_price is not None:
            set_price(product_name, new_price)

    elif action.lower() == "remove":
        # Check that the product name is in the list
        if product_name not in dairy_products and product_name not in meat_products:
            print("Product does not exist.")
            return
        # Remove the product from the appropriate list
        if category.lower() == "dairy":
            dairy_products.remove(product_name)
        else:
            meat_products.remove(product_name)

    elif action.lower() == "change":
        # Check that the product name is in the list
        if product_name not in dairy_products and product_name not in meat_products:
            print("Product does not exist.")
            return
        # Set the new price for the product
        if new_price is not None:
            set_price(product_name, new_price)
            # Update the price in the global list
            if product_name in dairy_products:
                dairy_products[dairy_products.index(product_name) + 1] = new_price
            else:
                meat_products[meat_products.index(product_name) + 1] = new_price

    else:
        print("Invalid action. Please choose either 'add', 'remove', or 'change'.")
        return

    # Print the updated list of products and prices for the category
    print("Updated list of {} products:".format(category))
    if category.lower() == "dairy":
        for i in range(0, len(dairy_products), 2):
            product = dairy_products[i]
            price = dairy_products[i + 1]
            print("{} - ${:.2f}".format(product, price))





def set_price(product_name, new_price):
    """
    Sets the price of a product.

    Parameters:
    product_name (str): The name of the product to set the price for.
    new_price (float): The new price of the product.

    Returns:
    None
    """
    # Here you would put the code to set the price of the product
    # This could involve looking up the product in a database, for example,
    # and updating the price in the database.

    # For this example implementation, we'll just print a message indicating
    # that the price has been updated.
    print("Price of {} has been updated to ${:.2f}.".format(product_name, new_price))
