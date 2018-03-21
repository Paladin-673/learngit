#!/usr/bin/python

import sys

base_count = 10000

for line in sys.stdin:
    index_id, key, val = line.strip().split('\t')
    
    new_key = int(key) - base_count

    print '\t'.jion(new_key, val)
