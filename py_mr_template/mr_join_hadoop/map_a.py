#!/usr/bin/python

import sys

for line in sys.stdin:
    ss = line.strip().split('\t')
    key = ss[0]
    val = ss[1]

    print "%s\t1\t%s" % (key, val)
