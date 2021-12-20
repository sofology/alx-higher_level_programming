#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Function for return if object is a instance inheritance"""
    return(type(obj) is not a_class and isinstance(obj, a_class))
