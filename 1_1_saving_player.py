"""
Python Homework for Online Python Course
by
Ibrahim Halil Bayat, PhD
Department of Electronics and Communication Engineering
Istanbul Technical University
Istanbul, Turkey
"""
print("...Saving the Player...")

name = input("Name of the player: ")
surname = input("Surname of the player: ")
team = input("Team of the player: ")

info = [name,  surname, team]
print("Saving the information...")
print("Name: {}\nSurname: {}\nTeam: {}".format(info[0], info[1], info[2]))
print("Process is finished.")