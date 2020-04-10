"""
Python Homework for Online Python Course
by
Ibrahim Halil Bayat, PhD
Department of Electronics and Communication Engineering
Istanbul Technical University
Istanbul, Turkey
"""
print("""
A program to check if the given number is a prime number.
Please enter q to exit.
""")
def prime_number(x):
    if x != 2 :
        for i in range(2,x):
            if x % i == 0:
                print("{} is not a prime number.".format(x))
                break
            else:
                print("{} is a prime number.".format(x))
                break
    if x == 2:
        print("{} is a prime number.".format(x))

while True:
    n = input("Please enter the number: ")
    if n == 'q':
        break
    else:
        prime_number(int(n))