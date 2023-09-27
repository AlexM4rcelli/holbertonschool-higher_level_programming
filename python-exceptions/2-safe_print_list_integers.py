#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len_list, printed = 0, 0
    while len_list < x:
        try:
            while len_list < x:
                print('{:d}'.format(my_list[len_list]), end="")
                len_list += 1
                printed += 1
        except (ValueError, TypeError):
            len_list += 1
            pass
    print()
    return printed
