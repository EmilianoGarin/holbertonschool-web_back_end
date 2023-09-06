#!/usr/bin/env python3
"""Task 8"""


def list_all(mongo_collection):
    """List all documents in the colection"""
    return list(mongo_collection.find())
