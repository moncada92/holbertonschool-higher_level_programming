#!/usr/bin/python3
for i in range(0, 58):
    if (i not in range(26, 32)):
        print("{:s}".format(chr(ord('z') - i)), end="")
