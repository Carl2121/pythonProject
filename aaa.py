import EXAM_MOD

school = "Palawan State University"
letter = school[5]
print(letter)


print("Welcome to BDO ATM")
username = input("Enter username: ")
print("Warning! You only have 5 attempts to enter your correct pin")
password = int(input("Enter 4-digit password: "))

attempts = 0
max_attempts = 5
out_of_attempts = False

while password != 2123 and not(out_of_attempts):
    if attempts < max_attempts:
        print("Wrong password, pls try again")
        password = int(input("Enter 4-digit password: "))
        attempts += 1

    else:
        out_of_attempts = True

if out_of_attempts == True:
    print("Insufficient attempts")

else:
    print("\nCorrect password! Welcome", username, "!")
    print("You currently have 5000 PHP")
    pick = int(input("What would you like to do?\n[1] Deposit\n[2] Withdraw\n[3] Cash Advance\n[4] Send Money\nEnter number here: "))

    if pick == 1:
        deposit = float(input("How much would you like to deposit?: "))
        EXAM_MOD.deposited(deposit)

    elif pick == 2:
        withdraw = float(input("How much would you like to withdraw? "))
        EXAM_MOD.withdrew(withdraw)

        if withdraw > 5000:
            choice = input("Insufficient money!, would you like to use our cash advance option? [Y/N]\nEnter Here: ").upper

            if choice == "Y":
                print("We have 0.05% annual interest")
                borrow = float(input("How much would you like to borrow?: "))
                EXAM_MOD.cash_adv(borrow)

            elif choice == "N":
                print("Thanks for banking with us! ")

            else:
                print("Invalid input")

    elif pick == 3:
        print("We have 0.05% annual interest")
        borrow = float(input("How much would you like to borrow?: "))
        EXAM_MOD.cash_adv(borrow)

    elif pick == 4:
        print("Choose the amount of money would you like to send: ")
        list = [[50], [100], [250], [500], [1000]]
        for i in list:
            print(i)

        amount = int(input("Enter amount"))
        receiver = input("Enter receiver: ")

        print("[CONFIRMATION] Are you sure you want to send", amount, "PHP to user @", receiver, "?")
        confirmation = input("[CONFIRMATION] Y/N: ").upper()

        if confirmation == "Y":
            print("You have sent", amount, "PHP to user @", username)
            print("Your remaining balance is", 5000 - amount, "PHP")

        elif confirmation == "N":
            print("Thank you for using our service!")

        else:
            print("Invalid input")


    else:
        print("Invalid input")




def deposited(deposit):
    print("You have deposited", deposit, "PHP")
    print("Your total balance is", 5000 + deposit, "PHP")

def withdrew(withdraw):
    print("You have withdrawn", withdraw, "PHP")
    print("Your total balance is", 5000 - withdraw, "PHP")

def borrowed(borrow):
    print("You have borrowed", borrow, "PHP")
    print("Your first annual interest will be", borrow * 0.05 * 1, "PHP")