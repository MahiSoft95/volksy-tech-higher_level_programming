#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = [0] * list_length
    for i in range(list_length):
        quotient = 0
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            newlist[i] = quotient
    return newlist
