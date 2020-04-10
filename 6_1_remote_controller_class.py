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


class class_remote_controller():
    def __init__(self, situation="Off", TV_volume=0, channel_list=["CNBC-E"], channel="CNBC-E"):
        self.situation = situation
        self.TV_volume = TV_volume
        self.channel_list = channel_list
        self.channel = channel

    def TV_on(self):
        if self.situation == 'On':
            print("TV is already On")
        else:
            print("Tv is opening...")
            self.situation = "On"

    def TV_off(self):
        if self.situation == 'Off':
            print("TV is already Off.")
        else:
            print("TV is closing...")
            self.situation = 'Off'

    def volume_action(self):

        while True:
            answer = input("""
            Volume Down: '<'
            Volume Up: '>'
            To exit: 'exit'
            """)
            if answer == '<' and self.TV_volume != 0:
                self.TV_volume -= 1
                print("Volume Down: ", self.TV_volume)

            elif answer == '>' and self.TV_volume != 35:
                self.TV_volume += 1
                print("Volume Up: ", self.TV_volume)
            else:
                print("The volume: ", self.TV_volume)
                break

    def add_channel(self, name_channel):
        print("Channel is adding...")
        time.sleep(1)
        self.channel_list.append(name_channel)

    def random_channel(self):
        rndm = random.randint(0, len(self.channel_list) - 1)
        self.channel = self.channel_list[rndm]
        print("the channel: ", self.channel)

    def __len__(self):
        return len(self.channel_list)

    def __str__(self):
        return """
        TV Situation: {}
        TV Volume: {}
        Channel List:{}
        Channel: {}
        """.format(self.situation, self.TV_volume, self.channel_list, self.channel)


print("""
****************
TV Application
Options: 
1- Open TV
2- Close TV
3- Volume Options
4- Add Channel 
5- Number of Channels 
6- Random Channel
7- TV Info
To exit please enter 'q'
***************
""")
obj_remote_controller = class_remote_controller()
while True:
    option = input("Please select the option: ")
    if option == 'q':
        print("Good Bye.")
        break
    elif option == '1':
        print("Open TV.")
        obj_remote_controller.TV_on()
    elif option == '2':
        print("Close TV.")
        obj_remote_controller.TV_off()
    elif option == '3':
        print("Volume options.")
        obj_remote_controller.volume_action()
    elif option == '4':
        print("Add channel.")
        user_list = input("Enter the channel by seperating with ','")
        user_channels = user_list.split(',')
        for adding_channel  in user_channels:
            obj_remote_controller.add_channel(adding_channel)

    elif option == '5':
        print("Number of channels: ", len(obj_remote_controller))

    elif option == '6':
        obj_remote_controller.random_channel()
    elif option == '7':
        print(obj_remote_controller)
    else:
        print("Please enter a valid option.")


        _

