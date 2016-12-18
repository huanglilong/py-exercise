#!/usr/bin/env python

import sys
import stddraw
from turtle import Turtle

def koch(n, step, turtle):
    if n == 0:
        turtle.goForward(step)
        return
    koch(n-1, step, turtle)
    turtle.turnLeft(60.0)
    koch(n-1, step, turtle)
    turtle.turnLeft(-120.0)
    koch(n-1, step, turtle)
    turtle.turnLeft(60.0)
    koch(n-1, step, turtle)

n = int(sys.argv[1])
stddraw.setPenRadius(0.0)
step = 3.0 ** -n 
turtle = Turtle(0.0, 0.0, 0.0)
koch(n, step, turtle)
stddraw.show()

