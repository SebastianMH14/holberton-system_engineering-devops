"""script to export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """list task to Employees"""
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id)).json()
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(id)).json()
    empty_users = {}
    empty_id = {}
    for users in user:
        user_id = users.get('id')
        empty_users[user_id] = []
        empty_id[user_id] = users.get('username')

    for todo in todos:
        id = todos.get("userId")
        aux = {}
        aux['task'] = todo.get('title')
        aux['completed'] = todo.get('completed')
        aux['username'] = empty_id.get(id)
        empty_users[id].append(aux)

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(empty_users, f)
