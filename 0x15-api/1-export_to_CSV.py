#!/usr/bin/python3
"""script to export data in the CSV format"""
import csv
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

    with open('{}.csv'.format(id), mode='w') as a:
        a_writer = csv.writer(a, quoting=csv.QUOTE_ALL)
        for task in todos:
            a_writer.writerow(
                [id, name, task.get('completed'), task.get('title')])
