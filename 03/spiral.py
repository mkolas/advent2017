import numpy

spiral = numpy.zeros((25,25))
spiral[13,13] = 1

x = 14
y = 13
direction = "right"

while(True):
    spiral[x,y] = spiral[x-1,y-1]+spiral[x,y-1]+spiral[x+1,y-1]+spiral[x-1,y]+spiral[x+1,y]+spiral[x-1,y+1]+spiral[x,y+1]+spiral[x+1,y+1]
    print(spiral[x,y])
    if direction == "right":
        if spiral[x,y-1] == 0:
            y = y-1
            direction = "up"
        else:
            x = x+1
        continue
    if direction == "up":
        if spiral[x-1,y] == 0:
            x = x-1
            direction = "left"
        else:
            y = y-1
        continue
    if direction == "left":
        if spiral[x,y+1] == 0:
            y = y+1
            direction = "down"
        else:
            x = x-1
        continue
    if direction == "down":
        if spiral[x+1,y] == 0:
            x = x+1
            direction = "right"
        else:
            y = y+1
        continue