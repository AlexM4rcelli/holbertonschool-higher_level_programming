#!/usr/bin/python3
def islower(c):
    return True if ord(c) >= 97 and ord(c) <= 122 else False


def uppercase(input_str):
    str_list = list(input_str)
    for i in range(len(str_list)):
        if islower(str_list[i]):
            up_letter = ord(str_list[i]) + ord('A') - ord('a')
            str_list[i] = chr(up_letter)
    print(''.join(str_list))
    return ''.join(str_list)
