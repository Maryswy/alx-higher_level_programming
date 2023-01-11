#!/usr/bin/python3

"""Module that looks up the attributes and methods of an object"""


def lookup(obj):
    """Lists available attributes and methods of an object"""
    return (list(dir(obj)))
