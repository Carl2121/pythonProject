# 1 Force of a moving object

#F = M * A

mass = float(input("Enter Mass: "))
acceleration = float(input("Enter Acceleration: "))

F = (mass * acceleration)
print("The force is", F, "N")


# 2 A program that computes the final grade of a student. It will ask the user to enter the GRADE in the Written Output and Performance Task.
# Written Output is 40%, Performance Task is 60%. Use the map() method.

WO, PT = map(float, input("Enter your Written Output and Performance Task respectively: ").split())

Written_Output = WO * 0.40
Performance_task = PT * 0.60

Final_Grade = Written_Output + Performance_task

print("Your final grade is", Final_Grade)


