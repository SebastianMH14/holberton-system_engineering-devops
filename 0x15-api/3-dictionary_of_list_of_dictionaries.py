#!/usr/bin/python3
"""script to export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":

    all_data = requests.get(
        "https://jsonplaceholder.typicode.com/users/")
    user = all_data.json()

    data = {}
    for users in user:
        f_data = []
        v = {"userId": users["id"]}
        todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos/", params=v)
        todos = todos.json()
        for todo in todos:
            f_data.append(
                {"username": users["username"], "task": todo["title"],
                    "completed": todo["completed"]})
        data[users['id']] = f_data

    with open("todo_all_employees.json", "w", newline="") as f:
        json.dump(data, f)
