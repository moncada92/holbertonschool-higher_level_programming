#!/usr/bin/env python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    count = len(args)
    itr = 1
    if count > 0:
        if count == 1:
            print("{:d} argument:".format(count))
        else:
            print("{:d} arguments:".format(count))
        for x in args:
            print("{:d}: {:s}".format(itr, x))
            itr += 1
    else:
        print("{:d} arguments.".format(count))
