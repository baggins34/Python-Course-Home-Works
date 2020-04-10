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
Welcome to the ATM Machine.
Options:
1) Check the amount.
2) Put money into the bank account.
3) Drawing cash.

Please enter q to exit.
*******************
""")

money = 1000

while True:
    option = input("Please select the option: ")
    if option == 'q':
        print("Good Bye.")
        break
    elif option == '1':
        print("Check the amount.")
        print("Amount of money: {}".format(money))
    elif option == '2':
        print("Putting cash into the acoount.")
        amount =float(input("Please enter the amount of money: "))
        money += amount
    elif option =='3':
        print("Drawing cash. ")
        amount = float(input("Please enter the amount of money: "))
        if money < amount:
            print("You don't have this much money.")
            continue
        money -= amount
    else:
        print("Please enter a valid option.")