#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        numbers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        num = 0
        for i in range(len(roman_string)):
            if roman_string[i] not in numbers:
                return 0
        for i in range(len(roman_string)):
            if (
                i < len(roman_string) - 1
                and numbers[roman_string[i]] < numbers[roman_string[i + 1]]
            ):
                num -= numbers[roman_string[i]]
            else:
                num += numbers[roman_string[i]]
        return num
    return 0
