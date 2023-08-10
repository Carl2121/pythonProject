idnum = int(input("Enter ID number: "))

lastname, firstname, mi = input("Enter lastname, firstname, and middle initial: ").split()
course = input("Enter Course: ").upper()


def tuitioncomp():


    if course == "BSCS":
        tuitionfee = 13500
        payment = float(input("Enter payment: "))
        a = payment - tuitionfee
        print(idnum, lastname, firstname, mi, "Remaining Balance: ", a)

    elif course == "BSIT":
        tuitionfee = 12500
        payment = float(input("Enter payment: "))
        a = payment - tuitionfee
        print(idnum, lastname, firstname, mi, "Remaining Balance: ", a)
    else:
        return 0

tuitioncomp()



