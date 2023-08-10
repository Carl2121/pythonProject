def leave():
    print("\nYOU'VE EXCEEDED YOUR ITEM LIMIT!")
    quit()


enter = input("Welcome!\nYou can only buy up to 5 items!")
again = True
buy_more = True
constant = True
quantity_apple = 0
quantity_mango = 0
quantity_guava = 0
quantity_pineapple = 0
quantity_sunkist = 0
pick_apple = False
pick_mango = False
pick_guava = False
pick_pineapple = False
pick_sunkist = False
cost = 0
item_limit = 5
pick_guide = True


while buy_more:
    print("\n")
#ANTI-ERROR INDICATOR
    if pick_guide:
        if pick_apple:
            print("YOU'VE ALREADY PICKED APPLE!")
        else:
            pass
        if pick_mango:
            print("YOU'VE ALREADY PICKED MANGO!")
        else:
            pass
        if pick_guava:
            print("YOU'VE ALREADY PICKED GUAVA!")
        else:
            pass
        if pick_pineapple:
            print("YOU'VE ALREADY PICKED PINEAPPLE!")
        else:
            pass
        if pick_sunkist:
            print("YOU'VE ALREADY PICKED SUNKIST!")
        else:
            pass
    else:
        pass

#PICK ITEM
    buy = input("What fruit would you like to buy?\n"
                "[PICKING THE SAME ITEM TWICE IS PROHIBITED!]\n"
                "    [A] Apple (Php 20)\n"
                "    [B] Mango (Php 10)\n"
                "    [C] Guava (Php 10)\n"
                "    [D] Pineapple (Php 40)\n"
                "    [E] Sunkist (Php 15)\n").upper()
#NUMBER OF ITEMS
    while again:
        if buy == "A":
            again = False
            print("\nHow many apples?\nUp to", item_limit, "more item/s")
            quantity_apple = int(input(""))
            item_limit = item_limit - quantity_apple
            if item_limit >= 0:
                cost = (quantity_apple * 20) + cost
                print("\nYou can buy", item_limit, "more item/s")
                pick_apple = True
            if item_limit == 0:
                cost = (quantity_apple * 20) + cost
                pick_apple = True
            elif item_limit < 0:
                leave()
        elif buy == "B":
            again = False
            print("\nHow many mangoes?\n Up to", item_limit, "more item/s")
            quantity_mango = int(input(""))
            item_limit = item_limit - quantity_mango
            if item_limit > 0:
                cost = (quantity_mango * 10) + cost
                print("\nYou can buy", item_limit, "more item/s")
                pick_mango = True
            if item_limit == 0:
                cost = (quantity_mango * 10) + cost
                pick_mango = True
            elif item_limit < 0:
                leave()
        elif buy == "C":
            again = False
            print("\nHow many guavas?\n Up to", item_limit, "more item/s")
            quantity_guava = int(input(""))
            item_limit = item_limit - quantity_guava
            if item_limit > 0:
                cost = (quantity_guava * 10) + cost
                print("\nYou can buy", item_limit, "more item/s")
                pick_guava = True
            if item_limit == 0:
                cost = (quantity_guava * 10) + cost
                pick_guava = True
            elif item_limit < 0:
                leave()
        elif buy == "D":
            again = False
            print("\nHow many pineapples?\n Up to", item_limit, "more item/s")
            quantity_pineapple = int(input(""))
            item_limit = item_limit - quantity_pineapple
            if item_limit > 0:
                cost = (quantity_pineapple * 40) + cost
                print("\nYou can buy", item_limit, "more item/s")
                pick_pineapple = True
            elif item_limit == 0:
                cost = (quantity_pineapple * 40) + cost
                pick_pineapple = True
            elif item_limit < 0:
                leave()
        elif buy == "E":
            again = False
            print("\nHow many sunkist?\n Up to", item_limit, "more item/s")
            quantity_sunkist = int(input(""))
            item_limit = item_limit - quantity_sunkist
            if item_limit > 0:
                cost = (quantity_sunkist * 15) + cost
                print("\nYou can buy", item_limit, "more item/s")
                pick_sunkist = True
            elif item_limit == 0:
                cost = (quantity_sunkist * 15) + cost
                pick_sunkist = True
            elif item_limit < 0:
                leave()
        else:
            buy = input("\nTry Again!\nWhat fruit would you like to buy?\n"
                        "[PICKING THE SAME ITEM TWICE IS PROHIBITED!]\n"
                        "    [A] Apple (Php 20)\n"
                        "    [B] Mango (Php 10)\n"
                        "    [C] Guava (Php 10)\n"
                        "    [D] Pineapple (Php 40)\n"
                        "    [E] Sunkist (Php 15)\n").upper()

    again = True

    if item_limit == 0:
        print("\nYou've reached your item limit!")
        buy_more = False
    elif item_limit < 5:
        buy_confirmation = 0
        del buy_confirmation
        constant = True
        buy_confirmation = input("Is there anything else? [Y/N]\n").upper()
        del buy
        while constant:
            if buy_confirmation == "Y":
                buy_more = True
                constant = False
            elif buy_confirmation == "N":
                buy_more = False
                constant = False
            else:
                buy_confirmation = input("\nTry Again!\nIs there anything else? [Y/N]\n").upper()

#RESULTS
print("\nYou total cost is Php", cost, "\nYou bought", quantity_apple, "apple/s (Php 20)\nYou bought", quantity_mango,
      "mango/es (Php 10)\nYou bought", quantity_guava, "guava/s (Php 10)\nYou bought", quantity_pineapple,
      "pineapple/s (Php 40)\nYou bought", quantity_sunkist, "sunkist/s (Php 15)")

