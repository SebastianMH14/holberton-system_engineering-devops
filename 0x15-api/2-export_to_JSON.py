#!/usr/bin/python3
"""script to export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """list task to Employees"""
    id = int(argv[1])
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id)).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(id)).json()
    name = user.get('username')

    data_dict = dict()
    data_list = list()
    for task in todos:
        title = task.get('title')
        status = task.get('status')
        final_dict = {"task": title, "completed": status, "username": name}
        data_list.append(final_dict)
        data_dict[id] = data_list

    with open('{}.json'.format(id), mode='w') as j:
        json.dump(data_dict, j)
