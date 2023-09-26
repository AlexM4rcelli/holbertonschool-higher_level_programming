#!/usr/bin/python3
def search_replace(my_list, search, replace):
    comp = lambda num : replace if num == search else num
    new = list(map(comp, my_list))
    return new
