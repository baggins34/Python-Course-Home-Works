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
weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))
bmi = weight / height**2
if bmi < 18.5:
    print("Underweight.")
if 18.5 <= bmi <= 25:
    print("Normal.")
if 25 < bmi <= 30:
    print("Overweight.")
if bmi > 30:
    print("Obese.")

# Problem 2
print("Problem 2: ")
a = float(input("Please enter your first number: "))
b = float(input("Please enter your first number: "))
c = float(input("Please enter your first number: "))
liste = [a,b,c]
print(max(liste))

# Problem 3
print("Problem 3: ")
md1 = float(input("Please enter the grade of the midterm 1: "))
md2 = float(input("Please enter the grade of the midterm 2: "))
fnl = float(input("Please enter the grade of the final: "))
gnl = 0.3*md1 + 0.3*md2 + 0.4*fnl
if gnl >= 90:
    print("AA")
elif gnl >= 85:
    print("BA")
elif gnl >= 80:
    print("BB")
elif gnl >= 75:
    print("CB")
elif gnl >= 70:
    print("CC")
elif gnl >= 65:
    print("DC")
elif gnl >= 60:
    print("DD")
elif gnl >= 55:
    print("FD")
else:
    print("FF")

# Problem 4
print("Problem 4: ")
user_answer = input("Please enter quad or triangle: ")
if user_answer == "quad":
    d1 = float(input("Please enter the first edge: "))
    d2 = float(input("Please enter the second edge: "))
    d3 = float(input("Please enter the third edge: "))
    d4 = float(input("Please enter the fourth edge: "))
    if d1 == d2 == d3 == d4 :
        print("It is a square.")
    elif d1 == d3 and d2 == d4:
        print("It is a rectangle.")
    else:
        print("It is just a quad")
elif user_answer == "triangle":
    t1 = float(input("Please enter the first edge of the triangle: "))
    t2 = float(input("Please enter the second edge of the triangle: "))
    t3 = float(input("Please enter the third edge of the triangle: "))
    if abs(t1-t2)<t3<t1+t2 and abs(t1-t3)<t2<t1+t3 and abs(t2-t3)<t1<t2+t3:
        if t1 == t2 == t3:
            print("It is a equilateral triangle.")
        elif t1 == t2 != t3 or t1 != t2 == t3 or t1 == t3 != t2:
            print("It is a right triangle.")
        else:
            print("It is just a triangle.")
    else:
        print("It is not a triangle.")