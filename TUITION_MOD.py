
def calculate_balance(tuitionfee, payment):
    return payment - tuitionfee

def tuitioncomp(idnum, lastname, firstname, mi, course):
    if course == "BSCS":
        tuitionfee = 13500
        payment = float(input("Enter payment: "))
        balance = calculate_balance(tuitionfee, payment)
        print(idnum, lastname, firstname, mi, "Remaining Balance: ", balance)

    elif course == "BSIT":
        tuitionfee = 12500
        payment = float(input("Enter payment: "))
        balance = calculate_balance(tuitionfee, payment)
        print(idnum, lastname, firstname, mi, "Remaining Balance: ", balance)