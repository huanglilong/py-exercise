#!/usr/bin/env python

import sys
import stddraw
import percolationv
import percolationio

n = int(sys.argv[1])
p = float(sys.argv[2])
trials = int(sys.argv[3])

for i in range(trials):
    isOpen = percolationio.random(n,p)
    stddraw.clear()
    stddraw.setPenColor(stddraw.BLACK)
    percolationio.draw(isOpen, False)
    stddraw.setPenColor(stddraw.BLUE)
    isFull = percolationv.flow(isOpen)
    percolationio.draw(isFull, True)
    stddraw.show(1000.0)
stddraw.show()

#
# ./visualiztionv.py 20 0.95 1
#
