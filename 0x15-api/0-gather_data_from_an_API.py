#!/usr/bin/python3
"""returns information about his/her TODO list progress."""
import requests
from sys import argv


if __name__ == "__main__":
    id = (argv[1])
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + id).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId=' + id).json()

    tareas = []
    for task in todos:
        if task.get('completed') is True:
            tareas.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}): ".
          format(user.get('name'), len(tareas), len(todos)))
    for task in tareas:
        print("\t {}".format(task))
