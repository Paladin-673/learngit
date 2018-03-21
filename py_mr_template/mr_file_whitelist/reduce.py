#!/usr/bin/python

import sys


def reducer_func():
    current_word = None
    count_pool = []
    sum = 0

    for line in sys.stdin:
        word,val = line.strip().split('\t')

        if current_word == None:
            current_word = word

        if current_word != word:
            for count in count_pool:
                sum += count
            print "%s\t%s" % (current_word,sum)
            current_word = word
            count_pool = []
            sum = 0

        count_pool.append(int(val))

    for count in count_pool:
        sum += count
    print "%s\t%s" % (current_word,str(sum))


if __name__ == "__main__":
    module = sys.modules[__name__]
    func = getattr(module,sys.argv[1])
    func()
