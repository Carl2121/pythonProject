# Fruit Store
# Cost of each fruit


Apple = int(20)
Mango = int(10)
Guava = int(10)
Pineapple = int(40)
Sunkist = int(15)

Fruits = input("What fruit would you like to buy?\n"
                "A.) Apple (20 php)\n"
                "B.) Mango (10 php)\n"
                "C.) Guava (10 php)\n"
                "D.) Pineapple (40 php)\n"
                "E.) Sunkist (15 php)\n").upper()


if Fruits == "A":
    Quantity = input("How many apples would you buy? ")
    Calculate1 = (Apple * int(Quantity))
    print(Calculate1, "PHP is the price lad\n")


if Fruits == "B":
    Quantity = input("How many mangoes would you buy? ")
    Calculate2 = (Mango * int(Quantity))
    print(Calculate2, "PHP is the price lad\n")


if Fruits == "C":
    Quantity = input("How many guavas would you buy? ")
    Calculate3 = (Guava * int(Quantity))
    print(Calculate3, "PHP is the price lad\n")


if Fruits == "D":
    Quantity = input("How many pineapples would you buy? ")
    Calculate4 = (Pineapple * int(Quantity))
    print(Calculate4, "PHP is the price lad\n")


if Fruits == "E":
    Quantity = input("How many sunkist would you buy? ")
    Calculate5 = (Sunkist * int(Quantity))
    print(Calculate5, "PHP is the price lad\n")


loop = True
while loop:
    if Fruits == "A" or Fruits == "B" or Fruits == "C" or Fruits == "D" or Fruits == "E":
        loop = False

    else:
        Fruits = input("Wrong Input! Try again and choose the letter of your fruit!\n")




Still_Buying = input("Would you still like to buy fruits?\n""Y/N\n").upper()


if Still_Buying == "Y".upper():
    print("You may continue to buy\n")

    Fruits = input("What fruit would you like to buy?\n"
                   "A.) Apple (20 php)\n"
                   "B.) Mango (10 php)\n"
                   "C.) Guava (10 php)\n"
                   "D.) Pineapple (40 php)\n"
                   "E.) Sunkist (15 php)\n").upper()

    if Fruits == "A":
        Quantity = input("How many apples would you buy? ")
        Calculate1 = (Apple * int(Quantity))
        print(Calculate1, "PHP is the price lad\n")

    if Fruits == "B":
        Quantity = input("How many mangoes would you buy? ")
        Calculate2 = (Mango * int(Quantity))
        print(Calculate2, "PHP is the price lad\n")

    if Fruits == "C":
        Quantity = input("How many guavas would you buy? ")
        Calculate3 = (Guava * int(Quantity))
        print(Calculate3, "PHP is the price lad\n")

    if Fruits == "D":
        Quantity = input("How many pineapples would you buy? ")
        Calculate4 = (Pineapple * int(Quantity))
        print(Calculate4, "PHP is the price lad\n")

    if Fruits == "E":
        Quantity = input("How many sunkist would you buy? ")
        Calculate5 = (Sunkist * int(Quantity))
        print(Calculate5, "PHP is the price lad\n")

    loop = True
    while loop:
        if Fruits == "A" or Fruits == "B" or Fruits == "C" or Fruits == "D" or Fruits == "E":
            loop = False

        else:
            Fruits = input("Wrong Input! Try again and choose the letter of your fruit!\n")


Still_Buying = input("Would you still like to buy fruits?\n""Y/N\n").upper()

if Still_Buying == "Y".upper():
    print("You may continue to buy\n")

#try making "if" function in this part
elif Still_Buying == "N".upper():
    print("Thank you for buying!")
    total = (int(Calculate1) + int(Calculate2))
    print(total, "php is the total")


else:
    print("Please choose either Y or N\n""Please try again!\n")































