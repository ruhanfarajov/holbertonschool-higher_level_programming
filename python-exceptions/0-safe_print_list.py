#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    nb_print = ""
    try:
        count  = 1
        for i in my_list:
            if count > x: 
                break
            nb_print += str(i)
            count += 1
    except Exception as e:
        print("{}".format(e))
    return int(nb_print)
