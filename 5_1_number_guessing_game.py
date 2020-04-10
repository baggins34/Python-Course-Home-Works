"""
Python Homework for Online Python Course
by
Ibrahim Halil Bayat, PhD
Department of Electronics and Communication Engineering
Istanbul Technical University
Istanbul, Turkey
"""
import random
import time

print("""
********************
Number guessing game.
Guess a number between 1 and 40.
You have 7 attempts. 
********************
""")

rand_number = random.randint(1, 40)
attemts = 7
while True:

    n = int(input("Have your guest: "))
    if n < rand_number:
        print("Checking....")
        time.sleep(1)
        print("Go higher.")
        attemts -= 1
    elif n > rand_number:
        print("Checking....")
        time.sleep(1)
        print("Get lower. ")
        attemts -= 1
    else:
        print("Checking....")
        time.sleep(1)
        print("Yeah you guessed right!")
        print(n)
        break
    if attemts == 0:
        print("Your right for attemts is over. The number is: ", n)