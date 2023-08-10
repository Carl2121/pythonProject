import loop

loop.add(4,3)
loop.minus(2,1)
loop.multiply(3,10)
loop.divide(5,2)



import random
digit = random.random()
print(digit)

import random
digit = random.uniform(1,10)
print(digit)

school = "Palawan State University"
m = school[2]
print(m)

lastchar = school[-1]
print(lastchar)

sentence = "python rocks"
print(sentence[2] + sentence[-4])

alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[5])

numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2])
print(numbers[9-8])
print(numbers[-2])

pet_names = ['Charlie', 'Max', 'Buddy', 'Milo', 'Reid',
'Blanket', 'Luna', 'Nixie', 'Yuki', 'Leo']
print(len(pet_names))

numbers = [17, 123, 87, 34, 66, 8398, 44]

a = (numbers[2])
b = (numbers[3])
c = (numbers[-1])

sum = (a + b + c)
print(sum)


desiderata = "Speak your truth quietly and clearly; and listen to  others,  even  to  the  dull  and  the  ignorant;  they  too  have their story."
excerpt_des = (desiderata[17:36])
print(excerpt_des)