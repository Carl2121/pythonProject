import TUITION_MOD

idnum = int(input("Enter ID number: "))
lastname, firstname, mi = input("Enter lastname, firstname, and middle initial: ").split()
course = input("Enter Course: ").upper()

TUITION_MOD.tuitioncomp(idnum, lastname, firstname, mi, course)
