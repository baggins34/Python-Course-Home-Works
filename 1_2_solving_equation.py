"""
Python Homework for Online Python Course
by
Ibrahim Halil Bayat, PhD
Department of Electronics and Communication Engineering
Istanbul Technical University
Istanbul, Turkey
"""

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - 4*a*c
x1 = (-b - delta**0.5)/(2*a)
x2 = (-b +delta**0.5)/(2*a)
print("x1: {}, x2: {}".format(x1,x2))