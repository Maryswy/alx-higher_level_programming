#!/usr/bin/python3
"""Module that appends a file"""


def append_write(filename="", text=""):
    """Append a file"""
    with open(filename, mode='a', encoding='UTF-8') as append_write:
        append_write.write(text)
        return len(text)
