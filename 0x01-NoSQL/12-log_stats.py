#!/usr/bin/env python3
"""
retrieves statistics about Nginx logs stored in a MongoDB collection named nginx.
It calculates the total number of logs, counts the occurrences of each HTTP method,
and provides the count for a specific method and path.
"""


from pymongo import MongoClient

def get_nginx_stats():
    """ Connect to MongoDB """
    client = MongoClient("mongodb://localhost:27017")
    db = client["logs"]
    nginx_collection = db["nginx"]

    """ Get the total number of logs """
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    """ Get the count of each HTTP method """
    methods = [
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE"
    ]
    print("Methods:")

    method_counts = nginx_collection.count_documents({"method": method})
    for method in methods:
        print(f"\tmethod {method}: {method_counts}")

    get_status_logs = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{get_status_logs} status check")

    if __name__ == "__main__":
        get_nginx_stats()
