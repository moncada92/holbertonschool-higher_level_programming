#!/usr/bin/python3
def no_c(my_string):
    list_s = list(my_string)
    for i in list_s:
        if i == 'C' or i == 'c':
            del list_s[list_s.index(i)]

    get_str = "".join(list_s)
    return get_str
