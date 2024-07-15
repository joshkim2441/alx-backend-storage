#!/usr/bin/env python3
"""
 returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieves a list of schools that cover the specified topic.

    Args:
        mongo_collection: A PyMongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: A list of school documents matching the specified topic.
    """
    return list(mongo_collection.find({"topics": topic}))
