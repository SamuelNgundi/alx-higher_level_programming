#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    err = 0
    while err < x:
        try:
            print(my_list[err], end="")
            err += 1
        except IndexError:
            break
        print()
        return err
