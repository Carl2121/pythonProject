

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




#JIAN CODE
numbers = list(map(float, input("Enter the numbers: ").strip().split()))

def min(number):
    min_num = number[0]
    for N in number:
        if N < min_num:
            min_num = N
    return min_num


def max(number):
    max_num = number[0]
    for N in number:
        if N > max_num:
            max_num = N
    return max_num


print("Highest number:", max(numbers))
print("Lowest number:", min(numbers))