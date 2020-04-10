"""
Python Homework for Online Python Course
by
Ibrahim Halil Bayat, PhD
Department of Electronics and Communication Engineering
Istanbul Technical University
Istanbul, Turkey
"""
print("""
*****************
Finding the dividers of a given number.
Please enter q to exit.
""")

def divider(x):
    my_list = list()
    for i in range(1,x+1):
        if x%i == 0:
            my_list.append(i)
    print(my_list)

while True:
    n = input("Please enter the number: ")
    if n == 'q':
        print("Good Bye.")
        break
    else:
        divider(int(n))