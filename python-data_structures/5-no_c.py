#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for k in range(len(my_string)):
        if my_string[k] != 'c' or my_string[k] != 'C':
            new_str += my_string
    return new_str