#!/usr/bin/env python3
"""
Insert a document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection
    Args:
        mongo_collection: pymongo collection object
        **kwargs: key-value pairs for the document
    Returns:
        The new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
