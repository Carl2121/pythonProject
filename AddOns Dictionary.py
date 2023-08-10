#AddOns Dictionary.py
import Pizza

name = input('Enter the customers name: ')
preference = input("Preferred Pizza: ").capitalize()
print("Base: 450")

if preference == "Deluxe":
    for key in Pizza.DELUXE.keys():
        print(key)
    print("\n")
    bill = Pizza.deluxe() + 450
    FinalPizzaChoice = {"Name: ": name, "Pizza Preference: ": preference, "Total Bill: ": bill}
    for key, value in FinalPizzaChoice.items():
        print(key,value)


elif preference == "Special":
    for key in Pizza.SPECIAL.keys():
        print(key)
    print("\n")
    bill = Pizza.special() + 450
    FinalPizzaChoice = {"Name: ": name, "Pizza Preference: ": preference, "Total Bill: ": bill}
    for key, value in FinalPizzaChoice.items():
        print(key,value)


elif preference == "Primo":
    for key in Pizza.PRIMO.keys():
        print(key)
    print("\n")
    bill = Pizza.primo() + 450
    FinalPizzaChoice = {"Name: ": name, "Pizza Preference: ": preference, "Total Bill: ": bill}
    for key, value in FinalPizzaChoice.items():
        print(key,value)

else:
    print("Invalid Input!")


