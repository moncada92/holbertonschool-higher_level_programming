#!/usr/bin/python3
def element_at(my_list, idx):
    elements = len(my_list)
    if (idx < 0 or idx >= elements):
        return None

    item = my_list[idx]
    return item
