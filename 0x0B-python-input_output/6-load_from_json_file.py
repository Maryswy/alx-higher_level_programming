#!/usr/bin/python3
"""Module that creates object from a JSON file"""


import json


def load_from_json_file(filename):
    """Create object from a JSON file"""
    with open(filename, 'r', encoding='UTF-8') as read_json:
       json.load(read_json)
