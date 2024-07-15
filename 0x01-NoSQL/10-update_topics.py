#!/usr/bin/env python3.10
""" 10-update_topics """

def update_topics(mongo_collection, name, topics):
    """
     Updates the topics of a school document based on the school name.

    Args:
        mongo_collection: A PyMongo collection object.
        name (str): The name of the school to update.
        topics (list): A list of topics to set for the school.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    try:
        result = mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
        return result.modified_count > 0
    except Exception as e:
        print(f"Error updating topics for {name}: {e}")
        return False
