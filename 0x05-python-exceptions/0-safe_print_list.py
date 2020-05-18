#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while x > count:
            print("{:d}".format(my_list[count]), end="")
            count += 1
    except TypeError:
        print("in the list have string")
    except IndexError:
        x = count
    print("")
    return count
