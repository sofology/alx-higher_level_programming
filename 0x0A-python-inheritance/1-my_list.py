#!/usr/bin/python3
class MyList(list):
    """Class my list por inherance"""
    pass

    def print_sorted(self):
        """function for print a list in ascending order"""
        print(sorted(list(self)))
