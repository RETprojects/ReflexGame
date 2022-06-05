import time
import thumby
import math

# Set the FPS (without this call, the default fps is 30)
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

#Randomly determine which shape the player should react to.
shape_name = ""


#Display the title of the game and the name of the shape to look out for.


#Black out the screen, then flash a shape at random.
