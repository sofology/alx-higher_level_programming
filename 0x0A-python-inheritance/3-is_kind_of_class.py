#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """Function for return True if the objec is a instance"""
    return(type(obj) is a_class or isinstance(obj, a_class))
