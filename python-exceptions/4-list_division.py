#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    index = 0
    while index < list_length:
        try:
            div = my_list_1[index] / my_list_2[index]
            index += 1
        except ZeroDivisionError:
            print("division by 0")
            div = 0
            index += 1
            continue
        except (TypeError, ValueError):
            print("wrong type")
            div = 0
            index += 1
            continue
        except IndexError:
            print("out of range")
            div = 0
            index += 1
            continue
        finally:
            result_list.append(div)
    return result_list
