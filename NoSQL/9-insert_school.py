#!/usr/bin/env python3
"""Task 9"""


def insert_school(mongo_collection, **kwargs):
    """add a document in the data base with kwargs"""
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id
