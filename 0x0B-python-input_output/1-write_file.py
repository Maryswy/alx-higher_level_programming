#!/usr/bin/python3
"""Module that writes to a file"""


def write_file(filename="", text=""):
    """Write to a file"""
    with open(filename, mode="w", encoding="utf-8") as write_file:
        new_write = write_file.write(text)
        return len(text)
