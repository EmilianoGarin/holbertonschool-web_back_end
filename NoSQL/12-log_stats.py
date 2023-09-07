#!/usr/bin/env python3
"""Task 12"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total = collection.count_documents({})

    method_counts = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    for k in method_counts.keys():
        method_counts[k] = collection.count_documents({"method": k})

    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{total} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")
