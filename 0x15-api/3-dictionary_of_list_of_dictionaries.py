"""script to export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    """list task to Employees"""
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()

    data = {}
    for users in user:
        data_list = []
        tareas = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format
            (users.get('id'))).json()

    for task in tareas:
        name = users.get('username')
        title = task.get('title')
        status = task.get('completed')
        my_dict = {"username": name, "task": title, "completed": status}
        data_list.append(my_dict)
        data[users.get('id')] = data_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(data, f)
