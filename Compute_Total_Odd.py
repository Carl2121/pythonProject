#Compute_Total_Odd


def odd(n):
    if n == 1:
        return [1]
    else:
        lists = odd(n - 1)
        if n % 2 != 0:
            lists.append(n)
        return lists

n = int(input("Input: "))

odd_numbers_list = odd(n)
odd_numbers_list_filtered = list(filter(lambda x: x % 2 != 0, odd_numbers_list))

print("Odd Numbers: ", odd_numbers_list_filtered)

odd_sum = sum(odd_numbers_list_filtered)
print("Total: ", odd_sum)



#Palindrome

