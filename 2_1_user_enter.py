"""
Python Homework for Online Python Course
by
Ibrahim Halil Bayat, PhD
Department of Electronics and Communication Engineering
Istanbul Technical University
Istanbul, Turkey
"""
print("""
*****************************
User Log in:
****************************
""")

user = "baggins34"
password = "1234"

user_input = input("Please enter your user name: ")
password_input = input("Please enter your password: ")

if user_input == user and password != password_input:
    print("Password is wrong.")
elif user_input != user and password == password_input:
    print("User name is wrong.")
elif user != user_input and password_input != password:
    print("User name and the password is wrong.")
else:
    print("Welcome.")
