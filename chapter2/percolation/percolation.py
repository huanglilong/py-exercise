#!/usr/bin/env python

import stdarray
import stdio

def _flow(isOpen, isFull, i, j):
    n = len(isFull)
    if (i < 0) or (i >= n): return  # out of range
    if (j < 0) or (j >= n): return 
    if not isOpen[i][j]: return     # blocked
    if isFull[i][j]: return         # already marked full

    isFull[i][j] = True             # mark full

    _flow(isOpen, isFull, i+1, j)   # down
    _flow(isOpen, isFull, i  , j+1) # right
    _flow(isOpen, isFull, i, j-1)   # left
    _flow(isOpen, isFull, i-1, j)   # up


def flow(isOpen):
    n = len(isOpen)
    isFull = stdarray.create2D(n, n, False)
    # flow computation goes here
    # init: get isOpen's top row
    for j in range(n):
        _flow(isOpen, isFull, 0, j)
    return  isFull

def percolates(isOpen):
    isFull = flow(isOpen)
    n = len(isFull)
    for j in range(n):
        if isFull[n-1][j]: return True
    return False

def main():
    isOpen = stdarray.readBool2D()
    stdarray.write2D(flow(isOpen))
    stdio.writeln(percolates(isOpen))

if __name__ == '__main__':
    main()
