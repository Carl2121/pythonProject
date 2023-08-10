#Test Recursive factorial
def factorial (n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial (5))


#Recursive Factorial
def factorial (n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial (5))

#Iterative factorial
def factorial (n):
    if n < 0:
        return -1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

print(factorial (5))


def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter number: "))
result = factorial(number)
print("The factorial of", number, "is", result)

