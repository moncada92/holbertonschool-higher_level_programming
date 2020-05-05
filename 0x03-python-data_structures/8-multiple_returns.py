#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        return 0, None
    size = len(sentence)
    first_l = sentence[:1]
    return (size, first_l)
