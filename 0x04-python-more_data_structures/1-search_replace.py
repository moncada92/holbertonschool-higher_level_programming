#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_l = my_list.copy()
    new_l[search - 1] = replace
    return new_l
