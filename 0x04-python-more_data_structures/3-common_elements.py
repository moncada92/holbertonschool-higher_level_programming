#!/usr/bin/python3
def common_elements(set_1, set_2):
    list_l = []
    for i in set_1:
        for j in set_2:
            if i == j:
                list_l.append(i)
    return list_l
