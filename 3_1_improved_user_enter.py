"""
Python Homework for Online Python Course
by
Ibrahim Halil Bayat, PhD
Department of Electronics and Communication Engineering
Istanbul Technical University
Istanbul, Turkey
"""
print("""
***********************************
Improved user log in program.
***********************************
""")

user = "baggins34"
password = "1234"
attempts = 3

while True:
    user_input = input("User name: ")
    password_input = input("Password: ")

    if user != user_input and password == password_input:
        print("User name is wrong.")
        attempts -= 1
    elif user == user_input and password_input != password:
        print("Password is wrong.")
        attempts -= 1
    elif user != user_input and password != password_input:
        print("Password and user name is wrong.")
        attempts -= 1
    else:
        print("welcome.")
        break
    if attempts == 0:
        print("No attempts left.")
        break