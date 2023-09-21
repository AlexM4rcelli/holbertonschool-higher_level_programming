#!/usr/bin/python3
for num in range(1, 100):
    if num == 89:
        print("{:02}".format(num))
    elif int(str(num)[0]) < (num % 10) or num < 10:
        print("{:02}".format(num), end=", ")
