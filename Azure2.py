

def findDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]

#print(findDuplicate([3,1,3,4,2]))

def findDuplicate2(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return num
        seen[num] = True

#print(findDuplicate2([3,1,3,4,2]))


import array

vals = array.array("i", [7,3,4,5,6,8])

"""""
vals.insert(3,10)
vals.append(14)
vals.remove(5)
del vals[0]
"""""

print(vals)



