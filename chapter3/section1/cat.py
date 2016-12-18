#!/usr/bin/env python

import sys
from instream import InStream
from outstream import OutStream

inFilenames = sys.argv[1:len(sys.argv)-1]
outFilename = sys.argv[len(sys.argv)-1]

outstream = OutStream(outFilename)
for filename in inFilenames:
    instream = InStream(filename)
    s = instream.readAll()
    outstream.write(s)
