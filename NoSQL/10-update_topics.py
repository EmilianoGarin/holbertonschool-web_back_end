#!/usr/bin/env python3
"""Task 10"""


def update_topics(mongo_collection, name, topics):
    """update topics"""
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, update)
