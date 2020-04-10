"""
Python Homework for Online Python Course
by
Ibrahim Halil Bayat, PhD
Department of Electronics and Communication Engineering
Istanbul Technical University
Istanbul, Turkey
"""
print("""
******************
Fibonacci 
******************
""")
n = int(input("Please enter the range: "))
a = 1
b = 1
fibonacci =[a,b]
for i in range(n+1):
    a,b = b, a+b
    fibonacci.append(b)
print(fibonacci)