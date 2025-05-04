#!/usr/bin/env python3
"""
Log stats - Nginx logs analysis
"""

from pymongo import MongoClient


def log_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx

    # Total number of logs
    total_logs = logs.count()
    print(f"{total_logs} logs")

    # Methods
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs.count({"method": method})
        print(f"\tmethod {method}: {count}")

    # Status check
    status_check = logs.count({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
 