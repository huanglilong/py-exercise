#!/usr/bin/env python

import sys
import stddraw
import estimate

def curve(n, x0, y0, x1, y1, trials=10000, gap=0.01, err=0.0025):
    xm = (x0+x1) / 2.0
    ym = (y0+y1) / 2.0
    fxm = estimate.evaluate(n, xm, trials)
    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(0.0)
        return
        
    # curve(n, x0, y0, xm, fxm)
    stddraw.filledCircle(xm, fxm, 0.005)
    stddraw.show(0.0)
    curve(n, x0, y0, xm, fxm)
    curve(n, xm, fxm, x1, y1)

n = int(sys.argv[1])
stddraw.setPenRadius(0.0)
curve(n, 0.0, 0.0, 1.0, 1.0)
stddraw.show()

#
# ./percplot.py 20
#
