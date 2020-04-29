#!/usr/bin/python3
def remove_char_at(str, n):
    letter = ""
    i = 0
    longs = len(str)
    if n < 0 or longs < n:
        return str

    while i < longs:
        if i == n:
            i += 1
            continue
        letter += str[i]
        i += 1
    return letter
