#!/usr/bin/env python3
"""
Retrieves statistics about Nginx logs stored in a
MongoDB collection named nginx.
It calculates the total number of logs, counts the
occurrences of each HTTP method,
and provides the count for a specific method and path.
"""


from pymongo import MongoClient

if __name__ == "__main__":
    """ Provide some stats about Nginx logs stored in MongoDB """
    client = MongoClient("mongodb://localhost:27017")
    nginx_collection = client.logs.nginx

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

    for method in methods:
        method_counts = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_counts}")

    get_status_logs = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f"{get_status_logs} status check")
