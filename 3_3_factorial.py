"""
Python Homework for Online Python Course
by
Ibrahim Halil Bayat, PhD
Department of Electronics and Communication Engineering
Istanbul Technical University
Istanbul, Turkey
"""

print("""
****************
Factorial Program

Please enter q to exit
******************
""")

while True:
    n = input("Please enter the number: ")
    if n == 'q':
        print("Good Bye.")
        break
    else:
        n = int(n)
        factorial = 1
        for i in range(2,n+1):
            factorial *= i
        print("Factorial: ", factorial)