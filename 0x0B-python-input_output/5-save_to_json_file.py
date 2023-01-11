#!/usr/bin/python3
"""Module that saves object as JSON to file"""


import json


def save_to_json_file(my_obj, filename):
    """Save object as JSON in a file"""
    with open(filename, mode='w', encoding='UTF-8') as new_write_json:
        json.dump(my_obj, new_write_json)
