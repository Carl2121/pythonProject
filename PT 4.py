#INPUT
pick = int(input("Enter Module Number from (1-3): "))

#PROCESS
#MODULE 1

if pick == 1:
    num = int(input("Enter the number: "))
    square = num**2
    cube = num**3
    print("Square", square)
    print("Cube", cube)

#MODULE 2

elif pick == 2:
    highest = smallest = 0
    counter = 1
    while counter <= 4:
        number = int(input("Enter number: " + str(counter) + "st integer: "))
        if counter == 1:
            highest = smallest = number
        if number > highest:
            highest = number
        if number < smallest:
            smallest = number

        counter += 1

    else:
        print("The highest number is", highest)
        print("The smallest number is", smallest)


#MODULE 3
elif pick == 3:
    name = input("Enter Name: ")
    year = int(input("Enter Year of Birth: "))
    month = int(input("Enter Birth Month Number: "))
    day = int(input("Enter day of Birth: "))

#Today is 10/28/2022

    age = 2022 - year
    birthMonth = 10 - month
    birthDay = 28 - day


    if age <= 17 and birthMonth <= 10 and birthDay <= 28:
        print(name, "is not qualified to vote for the election.")
    elif age >= 18:
        print(name, "is qualified to vote for the election.")
    else:
        print("Invalid Input")

else:
    print("Invalid Module Number")


