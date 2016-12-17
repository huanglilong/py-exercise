#!/usr/bin/env python

import sys
import stdio
import percolation
import percolationio

def evaluate(n, p, trials):
    count = 0
    for i in range(trials):
        isOpen = percolationio.random(n, p)
        if (percolation.percolates(isOpen)):
            count += 1
    return 1.0 * count / trials

def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    trials = int(sys.argv[3])
    q = evaluate(n, p, trials)
    stdio.writeln(q)

if __name__ == '__main__':
    main()

#
# ./estimate.py 20 0.65 100
#
