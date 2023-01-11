#!/usr/bin/python3
"""Module that returnd JSON to object"""


import json


def from_json_string(my_str):
    """JSON string to object"""
    return json.loads(my_str)

