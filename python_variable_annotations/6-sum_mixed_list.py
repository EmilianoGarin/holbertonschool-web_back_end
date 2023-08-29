#!/usr/bin/env python3
""" a type-annotated function sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float."""


def sum_mixed_list(a: list) -> float:
    """Takes a list of floats and int and returns their sum as a float"""
    ret = 0
    for v in a:
        ret += v
    return ret
