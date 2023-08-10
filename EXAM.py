import EXAM_MOD

print("Welcome to BDO atm!")
username = input("Enter Username: ")
print("Warning! You only have 5 attempts to enter your correct pin.")
password = int(input("Enter your four digit pin: "))


password_counter = 0
password_limit = 5
out_of_guesses = False

while password != 2123 and not out_of_guesses:

    if password_counter < password_limit:
        print("Wrong password!, please try again")
        password = int(input("Enter your four digit pin: "))
        password_counter += 1

    else:
        out_of_guesses = True

if out_of_guesses:
    print("Insufficient attempts")


else:
    print("\nCorrect Password!, Welcome", username)
    print("Your current balance is 5000 PHP")
    module_pick = int(input("What would you like to do?\n[1] Deposit money\n[2] Withdraw money\n[3] Cash Advance\n[4] Send money\nEnter number here: "))


    if module_pick == 1:
        deposit = float(input("Enter your deposit amount: "))
        EXAM_MOD.deposited(deposit)


    elif module_pick == 2:
        withdraw = float(input("Enter your withdrawal amount: "))

        if withdraw > 5000:
            cash_advance = input("Insufficient money, would you like to use our cash advance option? Y/N: ").upper()

            if cash_advance == "Y":
                print("We have 0.05% annual interest")
                borrow = float(input("Enter amount you want to borrow: "))
                borrowed_money = print("You borrowed", borrow, "PHP to the bank")
                EXAM_MOD.cash_adv(borrow)


            elif cash_advance == "N":
                print("Thank you for your using our ATM")

        else:
            EXAM_MOD.withdrew(withdraw)


    elif module_pick == 3:
        borrow = float(input("Enter amount you want to borrow: "))
        borrowed_money = print("You borrowed", borrow, "PHP to the bank")
        EXAM_MOD.cash_adv(borrow)



    elif module_pick == 4:
        print("\nChoose the amount of money you want to send")
        list = [[100], [250], [500], [750], [1000]]
        for i in list:
            print(i)


        amount = int(input("Enter amount: "))
        receiver = input("Enter username of receiver: ")

        print("\n[CONFIRMATION] Do you really want to send", amount, "PHP to user @", receiver, "?")

        confirmation = input("[CONFIRMATION] [Y/N]:  ").upper()

        if confirmation == "Y":
            print("You have sent", amount, "PHP to user @", receiver, ", your remaining balance is", 5000 - amount)

        else:
            print("Thank you for banking with us")

    else:
        print("Invalid input, please try again")














