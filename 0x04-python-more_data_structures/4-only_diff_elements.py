#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list_all = list(set_1) + list(set_2)
    list_l = []

    for i in set_1:
        for j in set_2:
            if i == j:
                list_l.append(i)

    for i in list_all:
        for j in list_l:
            if i == j:
                list_all.remove(i)
    
    return set(list_all) 
    
