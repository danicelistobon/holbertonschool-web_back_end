#!/usr/bin/env python3
""" Log stats module
"""
from pymongo import MongoClient


def get_logs(method: dict) -> int:
    """ gets logs
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs.count_documents(method)


def print_logs():
    """ provides some stats about Nginx logs stored in MongoDB
    """
    print(f"{get_logs({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_logs({'method': 'GET'})}")
    print(f"\tmethod POST: {get_logs({'method': 'POST'})}")
    print(f"\tmethod PUT: {get_logs({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {get_logs({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {get_logs({'method': 'DELETE'})}")
    print(f"{get_logs({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    print_logs()
