

def main():
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
        main()

    elif Still_Buying == "N".upper():
        confirmation = input("Thank you for buying!\nWould you like the to know the total purchases you bought?\nY/N\n")

        if confirmation == "Y".upper():
            print("Enter each fruit price one by one. Just type 0 if you haven't bought that specific fruit")
            num1 = int(input("Enter price of Apple: "))
            num2 = int(input("Enter price of Mango: "))
            num3 = int(input("Enter price of Guava: "))
            num4 = int(input("Enter price of Pineapple: "))
            num5 = int(input("Enter price of Sunkist: "))

            print(num1 + num2 + num3 + num4 + num5, "PHP is the total price of your purchases")

        elif confirmation == "N".upper():
            print("Goodbye!")

        else:
            print("Please choose either Y or N")


        exit()


    else:
        print("Please choose either Y or N\n""Please try again!\n")
        main()




main()