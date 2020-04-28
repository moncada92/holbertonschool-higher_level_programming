#!/usr/bin/python3
for i in range(0, 10):
    for n in range(1, 10):
        if (n + i) < 10:
            if i != 8:
                print("{0:0d}{1:0d}, ".format(i, (n + i)), end="")
            else:
                print("{0:0d}{1:0d}".format(i, (n + i)))
