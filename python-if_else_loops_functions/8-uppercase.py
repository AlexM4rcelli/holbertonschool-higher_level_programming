#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) + ord('A') - ord('a'))
        print('{}'.format(letter), end='')
    print()
