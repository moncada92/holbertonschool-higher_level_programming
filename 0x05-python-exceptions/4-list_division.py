#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    maxV = list_length
    result = 0
    list_n = []
    for i in range(0, maxV):
        try:
            result = my_list_1[i] / my_list_2[i]
            list_n.append(result)
        except ZeroDivisionError:
            result = 0
            list_n.append(result)
            print("division by 0")
        except TypeError:
            result = 0
            list_n.append(result)
            print("wrong type")
        except IndexError:
            result = 0
            list_n.append(result)
            print("out of range")

    return list_n
