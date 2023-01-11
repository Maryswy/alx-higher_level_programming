#!/usr/bin/python3
"""Module that represents object as JSON"""


import json


def to_json_string(my_obj):
    """Represent object as JSON"""
    return json.dumps(my_obj)

