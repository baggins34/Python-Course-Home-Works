"""
Python Homework for Online Python Course
by
Ibrahim Halil Bayat, PhD
Department of Electronics and Communication Engineering
Istanbul Technical University
Istanbul, Turkey
"""
print("""
    Enter the number of the question.
    1, 2, 3, 4, 5, 6.
    Please enter q to exit.
    """)
while True:

    option = input("Question: ")
    if option == 'q':
        break
    else:
        option = int(option)
    if option == 1:
        # Problem 1
        print("Problem 1: ")
        number = int(input("Please enter the number: "))
        ref_number = 0
        for i in range(1, number):
            if number % i == 0:
                ref_number += i
        if ref_number == number:
            print("{} is a perfect number.".format(number))
        else:
            print("{} is not a perfect number.".format(number))
            continue
    elif option == 2:
        # Problem 2
        print("Problem 2: ")
        number_as_str = input("Please enter a number: ")
        power = len(number_as_str)
        my_list = list()
        ref_number = 0
        for i in number_as_str:
            my_list.append(int(i))
        for i in my_list:
            ref_number += i**power
        if ref_number == int(number_as_str):
            print("{} is an Armstrong number.".format(int(number_as_str)))
        else:
            print("{} is not an Armstrong number.".format(int(number_as_str)))

    elif option == 3:
        # Problem 3
        print("Problem 3: ")
        for i in range(1,11):
            print("********************")
            for j in range(1,11):
                print("{} x {} = {}".format(i,j,i*j))

    elif option == 4:
        # Problem 4
        print("Problem 4: ")
        print("Enter q to exit.")
        number = 0
        while True:
            n = input("Enter the number: ")
            if n == 'q':
                print("Good Bye.")
                break
            else:
                number += int(n)
            print(number)

    elif option == 5:
        # Problem 5
        print("Problem 5: ")
        for i in range(1,101):
            if i % 3 == 0:
                print(i)
            else:
                continue
    elif option == 6:
        # Problem 6
        print("Problem 6: ")
        print([i for i in range(1,101) if i % 2 ==0])
    else:
        print("Please enter a valid question number.")
        continue
