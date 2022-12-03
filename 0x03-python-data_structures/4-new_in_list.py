#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''Replaces an element in a list without modifying the original list

    Args:
        my_list: original list
        idx: index of element to replace
        element: new element to replace element at index idx with

    Returns:
        new list with old element at idx now replaced with new element
    '''
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list[:]
    new_list[idx] = element
    return new_list
