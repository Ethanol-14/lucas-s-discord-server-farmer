from pynput.keyboard import Key, Controller as KeyCon
from pynput.mouse import Button, Controller as MouseCon
import time

keyboard = KeyCon()
mouse = MouseCon()

prempos = 0

typedelay = 0.01
number = 0
typetime = 61

time.sleep(2)
while True:
    whattotype = "Python type test "
    number = number+1

    #snapshot the pointer's current coordinates
    prempos = mouse.position

    #set the pointer's position (specific to my computer)
    mouse.position = (-945, 675)

    #clicks left click
    mouse.press(Button.left)
    time.sleep(typedelay)
    mouse.release(Button.left)

    #moves back to original position
    mouse.position = prempos

    #clicks left click
    mouse.press(Button.left)
    time.sleep(typedelay)
    mouse.release(Button.left)

    #holds then releases key
    for char in whattotype:
        keyboard.press(char)
        time.sleep(typedelay)
        keyboard.release(char)
        time.sleep(typedelay)

    for char in str(number):
        keyboard.press(char)
        time.sleep(typedelay)
        keyboard.release(char)
        time.sleep(typedelay)

    print("Typed: " + whattotype + str(number))

    keyboard.press(Key.enter)
    time.sleep(typedelay)
    keyboard.release(Key.enter)
    time.sleep(typedelay)
    print("hit enter")

    loop = typetime
    while loop > 0:
        time.sleep(1)
        print(loop)
        loop = loop-1