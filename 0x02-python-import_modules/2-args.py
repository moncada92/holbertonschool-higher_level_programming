#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    count = len(args)
    itr = 1
    if count > 0:
        print("{:d} arguments:".format(count))
        for x in args:
            print("{:d}: {:s}".format(itr, x))
            itr += 1
    else:
        print("{:d} arguments.".format(count))
