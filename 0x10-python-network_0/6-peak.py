#!/usr/bin/python3

"""
Peak Module
"""


def find_peak(list_of_integers):
    """Function for find the best value in the list integers"""

    leng_list = len(list_of_integers)

    max_val = 0

    if leng_list is 0:
        return None

    for a in range(leng_list):
        if list_of_integers[a] > max_val:
            max_val = list_of_integers[a]

    return max_val
