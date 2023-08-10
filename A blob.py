
def power(base, exponent):
    result = 1
    for index in range(exponent):
        result = result * base
    return result

print(power(2,3))


balance = int(input("Enter your balance: "))

print("Your balance is: ", balance)

thousands = balance / 1000
hundreds = balance % 1000 / 100
tenths = balance % 1000 % 100 / 10
ones = balance % 1000 % 100 % 10 / 1


print("thousands:",int(thousands))
print("hundreds:", int(hundreds))
print("tenths:", int(tenths))
print("ones:", int(ones))
      




