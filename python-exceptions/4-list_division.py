#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    result, i = 0, 0
    while i < list_length:
        try:
            while i < list_length:
                result = my_list_1[i] / my_list_2[i]
                new.append(result)
                i += 1
        except ZeroDivisionError:
            print('division by 0')
            new.append(0)
            pass
        except TypeError:
            print('wrong type')
            new.append(0)
            pass
        except IndexError:
            new.append(0)
            print('out of range')
            return new
        finally:
             i += 1
    return new
