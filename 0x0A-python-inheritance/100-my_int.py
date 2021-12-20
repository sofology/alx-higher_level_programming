#!/usr/bin/python3
"""MyInt class inherts of int"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, value):
        """Method for not equal"""
        return False

    def __ne__(self, value):
        """Method not equal to equal"""
        return True
