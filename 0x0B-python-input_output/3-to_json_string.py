#!/usr/bin/python3
""" Return JSON Representation of an object"""
import json


def to_json_string(my_obj):
    """Return a JSON representation of an object"""
    return json.dumps(my_obj)
