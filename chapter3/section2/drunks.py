#!/usr/bin/env python

import sys
import stdarray
import stddraw
import stdrandom
from turtle import Turtle

n = int(sys.argv[1])
trials = int(sys.argv[2])
step = float(sys.argv[3])
stddraw.setPenRadius(0.0)
turtles = stdarray.create1D(n)
for i in range(n):
    x = stdrandom.uniformFloat(0.0, 1.0)
    y = stdrandom.uniformFloat(0.0, 1.0)
    turtles[i] = Turtle(x, y, 0.0)

for t in range(trials):
    for i in range(n):
        angle = stdrandom.uniformFloat(0.0, 360.0)
        turtles[i].turnLeft(angle)
        turtles[i].goForward(step)
        stddraw.show(0)

stddraw.show()
