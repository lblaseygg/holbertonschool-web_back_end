#!/usr/bin/env python3
"""
Update topics of a school document
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document
    Args:
        mongo_collection: pymongo collection object
        name: school name to update
        topics: list of topics
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
