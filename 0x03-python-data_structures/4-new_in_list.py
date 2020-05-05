#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    elements = len(my_list)
    n_list = my_list.copy()

    if (idx >= 0 and idx < elements):
        n_list[idx] = element

    return n_list
