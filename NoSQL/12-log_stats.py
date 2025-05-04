#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def nginx_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB:
    - Number of logs
    - Count of each HTTP method
    - Number of status checks
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Access the logs database and nginx collection
    nginx_collection = client.logs.nginx
    
    # Get the total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Count documents for each HTTP method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")
    
    # Count documents for status check
    status_checks = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_checks} status check")


if __name__ == "__main__":
    nginx_stats()
