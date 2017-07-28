#! python3

#This will be my first foray into the land of text adventure games.

import actions, time, sys

#TODO Provide the setting

setting = "You wake up to find yourself covered in blood. You remember you are on a space station. Your name is Jack Harrington and you are a scientist stationed here for research. You are in the barracks where the other researchers sleep; however, there is no one to be seen."

available_actions = "\n \n Actions: \n -Scream \n -Look Around \n -Try to Remember"

def slow_print(text): #Function for slowly printing the text
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)

slow_print(setting) #Set the situation

print(available_actions)

action = input("What do you do?: ")
if action == "Scream":
    actions.scream()
elif action == "Look Around":
    actions.look_around()
elif action == "Try to Remember":
    actions.try_to_remember()
else:
    print("Please enter one of the provided commands")
    print(available_actions)
