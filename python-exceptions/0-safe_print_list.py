#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        nb_print = 0
        s = ''
        for i in my_list:
            if nb_print >= x:
                break
            s += str(i)
            nb_print += 1
        print(s)

    except Exception as e:
        print("{}".format(e))
    return nb_print
