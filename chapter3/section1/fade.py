#!/usr/bin/env python

import sys
import stddraw
from color import Color
from picture import Picture

def blend(c1, c2, alpha):
    r = (1- alpha) * c1.getRed() + alpha * c2.getRed()
    g = (1- alpha) * c1.getGreen() + alpha * c2.getGreen()
    b = (1- alpha) * c1.getBlue() + alpha * c2.getBlue()
    return Color(int(r), int(g), int(b))

sourceFile = sys.argv[1]
targetFile = sys.argv[2]
n = int(sys.argv[3])

source = Picture(sourceFile)
target = Picture(targetFile)

width = source.width()
height = source.height()

stddraw.setCanvasSize(width, height)

pic = Picture(width, height)

for t in range(n+1):
    for col in range(width):
        for row in range(height):
            c0 = source.get(col, row)
            cn = target.get(col, row)
            alpha = 1.0 * t / n
            pic.set(col, row, blend(c0, cn, alpha))
    stddraw.picture(pic)
    stddraw.show(1000.0)
stddraw.show()
