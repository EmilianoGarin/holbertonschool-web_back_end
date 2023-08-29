#!/usr/bin/env python3
""" a type-annotated function sum_list which takes a list input_list
of floats as argument and returns their sum as a float"""


def sum_list(a: list) -> float:
    """Takes a list of floats and returns their sum as a float"""
    ret = 0
    for v in a:
        ret += v
    return ret
