#!/usr/bin/python

import sys

for line in sys.stdin:
    ss = line.strip().split('\t')
    key = ss[0]
    index = ss[1]
    val = ss[2]

    print "%s\t%s\t%s" % (key, index, val)
