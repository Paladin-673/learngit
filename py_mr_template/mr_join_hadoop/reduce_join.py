#!/usr/bin/python

import sys

val_1 = []

for line in sys.stdin:
    key, flag, val = line.strip().split('\t')
    
    if flag == '1':
        val_1.append(val)
    elif flag == '2' and val_1 != "":
        val_2 = val

        for v in val_1:
            print "%s\t%s\t%s" % (key, v, val_2)
            val_1 = []
    else:
        val_2 = "NULL"

        for v in val_1:
            print "%s\t%s\t%s" % (key, v, val_2)
            val_1 = []
