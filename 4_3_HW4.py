"""
Python Homework for Online Python Course
by
Ibrahim Halil Bayat, PhD
Department of Electronics and Communication Engineering
Istanbul Technical University
Istanbul, Turkey
"""
print("""
HomeWork 4 
by 
Ibrahim Halil Bayat.
Enter the number of the question;
1, 2, 3, 4, 5.
Please enter q to exit.
""")
while True:
    option = input("Please enter the number of the question: ")
    if option == 'q':
        print("Good Bye.")
        break
    elif option == '1':
        # Problem 1
        print("Problem 1: ")
        def perfect_number(x):
            my_list = list()
            for i in range(1, x):
                my_number = 0
                for j in range(1,i):
                    if i % j == 0:
                        my_number += j
                if i == my_number:
                    my_list.append(my_number)
            print(my_list)

        a = int(input("Please enter the number: "))
        perfect_number(a)

    elif option == '2':
        n1 = int(input("Please enter the first number for EBOB: "))
        n2 = int(input("Please enter the second number for EBOB: "))
        def ebob(a,b):
            set_a = set()
            set_b = set()
            for i in range(1, a+1):
                if a % i == 0:
                    set_a.add(i)
            for i in range(1, b+1):
                if b % i == 0:
                    set_b.add(i)
            my_list = list(set_b.intersection(set_a))
            return max(my_list)
        print("The EBOB of {} and {} is {}".format(n1, n2, ebob(n1, n2)))



    elif option == '3':
        n1 = int(input("Please enter the first number for EKOK: "))
        n2 = int(input("Please enter the second number for EKOK: "))
        def ekok(a,b):
            ekok = 1
            i = 2
            while True:
                if a % i == 0 and b % i == 0:
                    ekok *= i
                    a //= i
                    b //= i
                elif a % i == 0 and b % i != 0:
                    ekok *= i
                    a //= i
                elif b % i == 0 and a % i != 0:
                    ekok *= i
                    b //= i
                else:
                    i += 1
                if a == 1 and b == 1:
                    break
            return ekok





        print("The EKOK of {} and {} is {}".format(n1, n2, ekok(n1, n2)))

    elif option == '4':
        # Problem 4
        print("Problem 4: ")
        n = int(input("Please enter a two-digit integer: "))
        def read_number(a):
            first = ["", "one", "two", "three", "four", "five", "six", "seven"
                     , "eight", "nine"]
            second =["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty",
                     "seventy", "eighty", "ninety"]
            other_second=["", "eleven", "twelve", "thirteen", "fourteen",
                          "fifteen", "sixteen", "seventeen", "eighteen",
                          "nineteen"]
            first_number = a%10
            second_number = a//10
            if second_number == 1 and first_number != 0:
                print(other_second[first_number])
            else:
                print(second[second_number] +" "+ first[first_number])
        read_number(n)



    elif option == '5':
        def pisagor(x):
            print([(i,j,z) for i in range(1, x+1) for j in range(i,x+1)
                   for z in range(j, x+1) if i**2 + j**2 == z**2])
        a = int(input("Please enter an integer: "))
        pisagor(a)
    else:
        print("Please enter a valid number for questions; 1, 2, 3, 4, 5")
        print("Please enter q to exit.")
        continue