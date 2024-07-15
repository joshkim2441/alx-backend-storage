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
    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = {
        "GET": 0,
        "POST": 0,
        "PUT": 0,
        "PATCH": 0,
        "DELETE": 0,
        "HEAD": 0
    }
    method_counts = {method: nginx_collection.count_documents(
        {"method": method}) for method, nginx_collection in methods.items()}
    get_status_logs = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in method_counts:
        print(f"\t{method}: {method_counts[method]}")
    print(f"GET /status: {get_status_logs}")

    if __name__ == "__main__":
        get_nginx_stats()
