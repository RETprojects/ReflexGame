#RETprojects
#June 4, 2022
#This is a MicroPython program, designed for the Thumby, to test the player's reaction time.

import thumby
import time

shape_name = ""
#Randomly choose a shape for the player to react to.


#Display the home screen and the name of the target shape.
thumby.display.fill(0) # Fill canvas to black
thumby.display.drawText("REFLEX", 5, 5, 1)
thumby.display.drawText("watch for a " + shape_name, 5, 15, 1)
thumby.display.drawText("press B to start", 5, 20, 1)
#Start the game when the player presses the start button.


def gameplay():


def drawCircle():


def drawRect():


def drawTriangle():


