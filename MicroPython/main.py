"""
Created by: Noah
Created on: March 2026
This module is a Micro:bit MicroPython program that runs a simple cookie clicker game
"""

from microbit import *


# setting up for game
display.clear()
display.show(Image.HAPPY)

cookies = 0

# starting the game
while True:
    if button_a.is_pressed():
        cookies = cookies + 1
    display.cookies

    # resetting game
if button_b.is_pressed():
    cookies = 0
    display.clear()
    display.cookies
