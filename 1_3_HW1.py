"""
Python Homework for Online Python Course
by
Ibrahim Halil Bayat, PhD
Department of Electronics and Communication Engineering
Istanbul Technical University
Istanbul, Turkey
"""
# Problem 1
print("Problem 1: ")
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
print("You entered: {}, {}, {}, and the multiplication of these three numbers is: {}".format(a,b,c,a*b*c))

# Problem 2
print("Problem 2: ")
weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))
print("Your weight is: {}, your height is: {}, your BMI (Body Mass Index) is: {}"
      .format(weight, height, weight/height**2))

# Problem 3
print("Problem 3: ")
dolar_per_mile = float(input("Please enter how much dollars your car needs per mile: "))
mile = float(input("Please enter the mile: "))
print("You have to pay: {} dollars.".format(dolar_per_mile*mile))

# Problem 4
print("Problem 4: ")
name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
number = input("Please enter your number: ")
print("""
Name: {}
Surname: {}
Number: {}
""".format(name, surname, number))

# Problem 5
print("Problem 5: ")
a1 = float(input("Please enter the first number: "))
a2 = float(input("Please enter the second number: "))
print("You entered: {}, {}".format(a1, a2))
a1, a2 = a2, a1
print("The new values are: {}, {}".format(a1, a2))

# Problem 6
print("Problem 6: ")
t1 = float(input("Please enter the first edge of the triangle: "))
t2 = float(input("Please enter the second edge of the triangle: "))
t3 = (t1**2 + t2**2)**0.5
print("The length of the third edge is: {}".format(t3))
