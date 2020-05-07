#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_l = my_list.copy()
    for i in new_l:
        if i == search:
            new_l[new_l.index(search)] = replace
    return new_l
