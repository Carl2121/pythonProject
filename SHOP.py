cost_list = list()
print("Price List\nA = Apple(20php)\nB = Banana(50php)\nC = Calamansi(100php)\n")
quantity = int(input("How many will you buy from the three products?: "))
while quantity != 0:
    pick = input('\nChoose one item from [A, B, C]\n').upper()

    if pick == "A":
        quantity_a = int(input("Enter quantity of Apple: "))
        cost_a = 20 * quantity_a
        cost_list.append(cost_a)
        quantity -= 1

    elif pick == "B":
        quantity_b = int(input("Enter quantity of Banana: "))
        cost_b = 50 * quantity_b
        cost_list.append(cost_b)
        quantity -= 1

    elif pick == "C":
        quantity_c = int(input("Enter quantity of Calamansi: "))
        cost_c = 100 * quantity_c
        cost_list.append(cost_c)
        quantity -= 1

    else:
        retry = input("Wrong Input, Would you like to try again? type Y/N: ").upper()
        if retry == "Y":
            quantity += 1
        else:
            quit()

cost_total = 0
for i in range(len(cost_list)):
    cost_total = cost_total + cost_list[i]
print("\nTotal cost is ", cost_total)






