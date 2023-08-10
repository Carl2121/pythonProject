#Sequences and Series
#Input
a, b, c, d, e = map(float, input("Enter Sequence up to 5: ").split())

#First base
a1 = b - a
a2 = c - b
a3 = d - c
a4 = e - d

#Second base
a5 = a2 - a1
a6 = a3 - a2
a7 = a4 - a3

#Third base
a8 = a6 - a5
a9 = a7 - a6

if a1 == a2 == a3 == a4:
    print(a,b,c,d,e)
    sequence_type = "Arithmetic Series"
    print(sequence_type)
    print("The common difference is ", a1)
    term = float(input("Which nth term?: "))
    an = a + (term - 1) * a1
    print("The answer is", an)

elif (not a1 == a2 == a3 == a4) and a5 == a6 == a7:
    print(a,b,c,d,e)
    sequence_type = "Quadratic Series"
    print(sequence_type)
    print("The common difference is ", a5)
    term = float(input("Which nth term?: "))

#finding zeroth term or "C" for quadratic
    zeroth_term = a - (a1 - a5)
    print("The zeroth term is ", zeroth_term)
    solve_a = a5 / 2
    solve_b = (a1 - a5) - solve_a
    an = (solve_a * (term ** 2))+ (solve_b * term) + zeroth_term
    print("The answer is", an)


elif (not a1 == a2 == a3 == a4) and (not a5 == a6 == a7) and a8 == a9:
    print(a, b, c, d, e)
    sequence_type = "Cubic Series"
    print(sequence_type)
    print("The common difference is ", a8)
    term = float(input("Which nth term?: "))

#finding zeroth term or "D" for cubic
    zeroth_term = a - (a1 - (a5 -a8))
    print("The zeroth term is ", zeroth_term)
    solve_a = a8 / 6
    solve_b = ((a5 - a8) - a8) / 2
    solve_c = -1 * ((solve_a + solve_b) - (a1 - (a5 - a8)))

    an = (solve_a * (term**3)) + (solve_b * (term**2)) + (solve_c * term) + zeroth_term
    print("The answer is", an)

else:
    print("Only from Arithmetic, Quadratic, and Cubic chief!")







