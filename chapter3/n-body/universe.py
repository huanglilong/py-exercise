#!/usr/bin/env python

import sys
import stdarray
import stddraw
from body import Body
from instream import InStream
from vector import Vector

class Universe:
    def __init__(self, filename):
        instream = InStream(filename)
        n = instream.readInt()
        radius = instream.readFloat()
        stddraw.setXscale(-radius, radius)
        stddraw.setYscale(-radius, radius)
        self._bodyies = stdarray.create1D(n)

        for i in range(n):
            rx = instream.readFloat()
            ry = instream.readFloat()
            vx = instream.readFloat()
            vy = instream.readFloat()
            mass = instream.readFloat()
            r = Vector([rx, ry])
            v = Vector([vx, vy])
            self._bodyies[i] = Body(r, v, mass)
    
    def increaseTime(self, dt):
        n = len(self._bodyies)
        f = stdarray.create1D(n, Vector([0, 0]))
        # calculate all bodies's aggregate force
        for i in range(n):
            for j in range(n):
                if i != j:
                    bodyi = self._bodyies[i]
                    bodyj = self._bodyies[j]
                    f[i] += bodyi.forceFrom(bodyj)
        # update all bodies's position and velocity
        for i in range(n):
            self._bodyies[i].move(f[i], dt)
        
    def draw(self):
        for body in self._bodyies:
            body.draw()

def main():
    universe = Universe(sys.argv[1])
    dt = float(sys.argv[2])
    while True:
        universe.increaseTime(dt)
        stddraw.clear()
        universe.draw()
        stddraw.show(10)

if __name__ == '__main__':
    main()

    