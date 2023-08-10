# While loop
loop = 1
while loop <= 10:
    print(loop)
    loop += 1

# For loop


for i in range(10):
    if i == 0:
        continue
    print(i)



row = 5

for i in range(1, row + 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")




name = input("Enter the name: ")

loop = 1
while loop <= 5:
    print(name)

    loop += 1


loop = 2
while loop <= 20:
    print(loop)

    loop += 2

loop = 50
while loop >= 0:
    print(loop)

    loop -= 10



