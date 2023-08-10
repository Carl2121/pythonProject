first, second, third, fourth = map(int, input('Enter the four integers: ').split())
print("Entered integers: ", first, second, third, fourth)

if first < second < third < fourth or second > first > third > fourth:
    print(first, "is the lowest number")
    print(second,"is the highest number")

elif second > first < third and first < fourth or first < third > second and third > fourth:
    print(first, "is the lowest number")
    print(third, "is the highest number")

elif second > first < third and first < fourth or first < third > second and third > fourth:
    print(first, "is the lowest number")
    print(fourth, "is the highest number")

elif first > second < third and second < fourth or second < first > third and first > fourth:
    print(second, "is the lowest number")
    print(first, "is the highest number")

elif first > second < third and second < fourth or first < third > second and third > fourth:
    print(second, "is the lowest number")
    print(third, "is the highest number")

elif first > second < third and second < fourth or first < third > second and third > fourth:
    print(second, "is the lowest number")
    print(fourth, "is the highest number")

elif first > third < second and third < fourth or second < first > third and first > fourth:
    print(third, "is the lowest number")
    print(first, "is the highest number")

elif first > third < second and third < fourth or first < second > third and second > fourth:
    print(third, "is the lowest number")
    print(second, "is the highest number")

elif first > third < second and third < fourth or first < third > second and third > fourth:
    print(third, "is the lowest number")
    print(fourth, "is the highest number")

elif first > fourth < second and fourth < third or second < first > third and first > fourth:
    print(fourth, "is the lowest number")
    print(first, "is the highest number")

elif first > fourth < second and fourth < third or first < second > third and second > fourth:
    print(fourth, "is the lowest number")
    print(second, "is the highest number")

elif first > fourth < second and fourth < third or first < third > second and third > fourth:
    print(fourth, "is the lowest number")
    print(third, "is the highest number")

else:
    print("Invalid input")


first, second, third, fourth = map(int, input('Enter the four integers: ').split())
    print("Entered integers: ", first, second, third, fourth)

#FOR LOWEST NUMBER
    if second > first < third and first < fourth:
        print(first, "is the lowest number")
    elif first > second < third and second < fourth:
        print(second, "is the lowest number")
    elif first > third < second and third < fourth:
        print(third, "is the lowest number")
    elif first > fourth < second and fourth < third:
        print(fourth, "is the lowest number")
    else:
        print("Invalid Input")

#FOR HIGHEST NUMBER

    if second < first > third and first > fourth:
        print(first, "is the highest number")
    elif first < second > third and second > fourth:
        print(second, "is the highest number")
    elif first < third > second and third > fourth:
        print(third, "is the highest number")
    elif first < third > second and third > fourth:
        print(fourth, "is the highest number")
    else:
        print("Invalid Input")