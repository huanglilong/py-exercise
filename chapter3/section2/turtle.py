#!/usr/bin/env python

import math
import sys
import stddraw

class Turtle:
    def __init__(self, x0, y0, angle0):
        self._x = x0
        self._y = y0
        self._angle = angle0
    
    def turnLeft(self, delta):
        self._angle += delta
    
    def goForward(self, step):
        oldx = self._x
        oldy = self._y
        self._x += step * math.cos(math.radians(self._angle))
        self._y += step * math.sin(math.radians(self._angle))
        stddraw.line(oldx, oldy, self._x, self._y)
    
def main():
    n = int(sys.argv[1])
    step = math.sin(math.radians(180.0 / n))
    turtle = Turtle(0.5, 0.0, 180.0 / n)
    for i in range(n):
        turtle.goForward(step)
        turtle.turnLeft(360.0 / n)
    stddraw.show()

if __name__ == '__main__':
    main()
    