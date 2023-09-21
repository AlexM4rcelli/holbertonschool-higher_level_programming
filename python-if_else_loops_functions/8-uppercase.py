#!/usr/bin/python3
def uppercase(input_str):
    str_list = list(input_str)
    for i in range(len(str_list)):
        if ord(str_list[i]) >= 97 and ord(str_list[i]) <= 122:
            up_letter = ord(str_list[i]) + ord('A') - ord('a')
            str_list[i] = chr(up_letter)
    print(''.join(str_list))
