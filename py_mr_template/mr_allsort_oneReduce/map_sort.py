#!/usr/bin/python

import sys

base_count = 10000

for line in sys.stdin:
    ss = line.strip().split('\t')
    key = ss[0]
    val = ss[1]

    new_key = base_count + int(key)
    print "%s\t%s" % (new_key,val)

