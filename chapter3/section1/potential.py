#!/usr/bin/env python
import stddraw
import stdio
import stdarray
from charge import Charge
from color import Color
from picture import Picture

# get all charge's pos and value
n = stdio.readInt()
charges = stdarray.create1D(n)
for i in range(n):
    x0 = stdio.readFloat()
    y0 = stdio.readFloat()
    q0 = stdio.readFloat()
    charges[i] = Charge(x0, y0, q0)

pic = Picture(500, 500)
for col in range(pic.width()):
    for row in range(pic.height()):
        x = 1.0 * col / pic.width()
        y = 1.0 * row / pic.height()
        v = 0.0
        for i in range(n):
            v += charges[i].potentialAt(x, y)
        v = 255 / 2.0 + v / 2.0e10
        if v < 0:       gray = 0
        elif v > 255:   gray = 255
        else:           gray = int(v)
        color = Color(gray, gray, gray)
        pic.set(col, row, color)

stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.picture(pic)
stddraw.show()
