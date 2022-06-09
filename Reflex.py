import time
import thumby
import random
import sys

thumby.display.setFPS(60)

# VARIABLES, SPRITES, ETC.

# BITMAP: width: 16, height: 16
bitmapCircle = bytearray([224,248,252,254,254,255,255,255,255,255,255,254,254,252,248,224,
           7,31,63,127,127,255,255,255,255,255,255,127,127,63,31,7])

circleSprite = thumby.Sprite(16, 16, bitmapCircle)

# BITMAP: width: 16, height: 16
bitmapTriangle = bytearray([3,15,63,255,255,255,255,255,255,255,255,255,255,63,15,3,
           0,0,0,0,3,15,63,255,255,63,15,3,0,0,0,0])

triangleSprite = thumby.Sprite(16, 16, bitmapTriangle)

# BITMAP: width: 16, height: 16
bitmapSquare = bytearray([255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
           255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255])

squareSprite = thumby.Sprite(16, 16, bitmapSquare)

react_time = 0
begin = 0
end = 0
shape_name = ""

# FUNCTIONS

# This function begins recording the reaction time.
# If the A button is still pressed, it will wait until A is released to begin recording.
def beginStopwatch():
    global begin # this is needed to modify the global copy of begin
    begin = time.ticks_ms()
    while True:
        if not thumby.buttonA.pressed():
            break
    return

def drawCircle(x: int, y: int):
    circleSprite.x = x
    circleSprite.y = y
    thumby.display.drawSprite(circleSprite)
    thumby.display.update()
    return

def drawTriangle(x: int, y: int):
    triangleSprite.x = x
    triangleSprite.y = y
    thumby.display.drawSprite(triangleSprite)
    thumby.display.update()
    return

def drawSquare(x: int, y: int):
    squareSprite.x = x
    squareSprite.y = y
    thumby.display.drawSprite(squareSprite)
    thumby.display.update()
    return

# Randomly choose a shape to use for the game.
def chooseShape():
    global shape_name
    random.seed(time.ticks_ms()) # set the seed of the random number generator
    num = random.randint(0,2)
    if num == 0:
        shape_name = "circle"
    elif num == 1:
        shape_name = "triangle"
    else:
        shape_name = "square"
    return

def playGame():
    # Randomly determine which shape the player should react to.
    chooseShape()
    
    # Once the button is pressed to start the game, display the name of the shape to look out for.
    thumby.display.fill(0)
    thumby.display.drawText("press A for", 5, 5, 1)
    thumby.display.drawText("a " + str(shape_name), 5, 14, 1)
    thumby.display.drawText("U to start", 5, 27, 1)
    thumby.display.update()
    
    while True:
        if thumby.buttonU.pressed():
            break
    
    # Black out the screen, then flash a shape at random.
    while True:
        thumby.display.fill(0) # Fill canvas to black
        thumby.display.update()
        
        # Generate a random number to determine whether to display a shape.
        num = random.randint(0,100)
        # If the random number is 0, draw a shape in the center of the screen.
        if num == 0:
            num = random.randint(0,2) # to decide which shape to display
            if num == 0: # if 0, draw a circle
                drawCircle(int((thumby.display.width/2) - (16/2)), int((thumby.display.height/2) - (16/2)))
                if shape_name == "circle":
                    beginStopwatch()
                    break
                else:
                    time.sleep(1)
            elif num == 1: # if 1, draw a triangle
                drawTriangle(int((thumby.display.width/2) - (16/2)), int((thumby.display.height/2) - (16/2)))
                if shape_name == "triangle":
                    beginStopwatch()
                    break
                else:
                    time.sleep(1)
            else: # if 2, draw a square
                drawSquare(int((thumby.display.width/2) - (16/2)), int((thumby.display.height/2) - (16/2)))
                if shape_name == "square":
                    beginStopwatch()
                    break
                else:
                    time.sleep(1)
    
    # Get the time when the player reacts by pressing a button.
    while True:
        if thumby.buttonA.pressed():
            end = time.ticks_ms()
            thumby.display.fill(0) # get the shape off the screen
            thumby.display.update()
            break
    
    # Display the player's reaction time.
    react_time = end - begin # the reaction time in ms
    thumby.display.drawText("time:", 5, 5, 1)
    thumby.display.drawText(str(react_time) + "ms", 5, 14, 1)
    thumby.display.drawText("D to retry", 5, 23, 1)
    thumby.display.drawText("B to quit", 5, 32, 1)
    thumby.display.update()
    
    # Wait for the player to play again or quit the game.
    while True:
        if thumby.buttonD.pressed():
            playGame() # play again
        if thumby.buttonB.pressed():
            sys.exit() # exit the program
    
    return

# GAMEPLAY

# Display the title of the game.
thumby.display.fill(0)
thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
thumby.display.drawText("REFLEX", 5, 5, 1)
thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
thumby.display.drawText("D to play", 5, 18, 1)
thumby.display.drawText("B to quit", 5, 27, 1)
thumby.display.update()

while True:
    if thumby.buttonD.pressed():
        playGame()
    if thumby.buttonB.pressed():
        sys.exit() # exit the program
