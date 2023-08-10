def security():
    name = input("Enter Username: ")
    id = int(input("Enter User ID: "))
    password = int(input("Enter 4-digit password: "))
    pass_count = 1
    pass_limit = 5
    out_of_guesses = False
    while password != 4444 and not out_of_guesses:

        if pass_count < pass_limit:
            print("Wrong password! Try Again!")
            password = int(input("Enter 4-digit password: "))
            pass_count += 1

        else:
            out_of_guesses = True
            print("You ran out of attempts!")

    if password == 4444:
        print(f"Welcome {name} with user ID number: {id}")




def simple_security():
    name = input("Enter Username: ")
    id = int(input("Enter User ID: "))
    print(f"Welcome {name} with user ID number: {id}")


def list_security():
    lastname = input("Enter lastname: ")
    firstname = input("Enter firstname: ")
    mi = input("Enter middle inital: ")
    id = int(input("Enter student ID: "))
    course = input("Enter course: ")
    block = int(input("Enter Block Number: "))

    list = [lastname, firstname, mi, id, course, block ]
    print(list)


list_security()