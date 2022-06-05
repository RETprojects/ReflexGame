import time
import thumby
import math
import random

thumby.display.setFPS(60)

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
#Randomly determine which shape the player should react to.
shape_name = ""
num = random.randint(0,2)
if num == 0:
    shape_name = "circle"
elif num == 1:
    shape_name = "triangle"
else:
    shape_name = "square"

#Display the title of the game and the name of the shape to look out for.


thumby.display.fill(0)
circleSprite.x = int((thumby.display.width/2) - (16/2))
circleSprite.y = int((thumby.display.height/2) - (16/2))

#Black out the screen, then flash a shape at random.
while(1):
    thumby.display.fill(0) # Fill canvas to black
    
    #Generate a random number to determine whether to display a shape.
    num = random.randint(0,9)
    if num == 0:
        circleSprite.x = int((thumby.display.width/2) - (16/2))
        circleSprite.y = int((thumby.display.height/2) - (16/2))
        thumby.display.drawSprite(circleSprite)
        thumby.display.update()
        
        break

#Display the player's reaction time.
