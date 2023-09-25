#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return list(element for element in my_list)
    else:
        new = list(element for element in my_list)
        new[idx] = element
        return new
