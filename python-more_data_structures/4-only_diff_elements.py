#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diffs_1 = set(filter(lambda x: x not in set_2, set_1))
    diffs_2 = set(filter(lambda x: x not in set_1, set_2))
    return diffs_1.union(diffs_2)
