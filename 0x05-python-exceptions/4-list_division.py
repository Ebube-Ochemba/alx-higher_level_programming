#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    for obj in range(list_length):
        try:
            result[obj] = my_list_1[obj] / my_list_2[obj]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            continue
    return result
