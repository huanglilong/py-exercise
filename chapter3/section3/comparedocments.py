#!/usr/bin/env python

import sys
import stdarray
import stdio
from instream import InStream
from sketch import Sketch

k = int(sys.argv[1])
d = int(sys.argv[2])
filenames = stdio.readAllStrings()

sketches = stdarray.create1D(len(filenames))

for i in range(len(filenames)):
    text = InStream(filenames[i]).readAll()
    sketches[i] = Sketch(text, k, d)

stdio.write('       ')
for i in range(len(filenames)):
    stdio.writef('%8.4s', filenames[i])
stdio.writeln()

for i in range(len(filenames)):
    stdio.writef('%.4s', filenames[i])
    for j in range(len(filenames)):
        stdio.writef('%8.2f', sketches[i].similarTo(sketches[j]))
    stdio.writeln()
