#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(element for element in my_list)
    return sum(element for element in new)
