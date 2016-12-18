#!/usr/bin/env python

import sys
import stdarray
from instream import InStream
from outstream import OutStream

basename = sys.argv[1]
n = int(sys.argv[2])

instream = InStream(basename + '.csv')
out = stdarray.create1D(n)

for i in range(n):
    out[i] = OutStream(basename + str(i) + '.txt')

while instream.hasNextLine():
    line = instream.readLine()
    fields = line.split(',')
    for i in range(n):
        out[i].writeln(fields[i])

