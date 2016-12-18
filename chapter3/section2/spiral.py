#!/usr/bin/env python

import math
import sys
import stddraw
from turtle import Turtle

n = int(sys.argv[1])
wraps = int(sys.argv[2])
decay = float(sys.argv[3])
angle = 360.0 / n

step = math.sin(math.radians(angle / 2.0))
turtle = Turtle(0.5, 0.0, angle / 2.0)

stddraw.setPenRadius(0.0)
for i in range(wraps * n):
    step /= decay
    turtle.goForward(step)
    turtle.turnLeft(angle)

stddraw.show()
