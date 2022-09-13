#!/usr/bin/python3
"""call a REST API and display formatted response"""

import json
import requests
from sys import argv


def create_json():
    """
    fetches data from REST API and stores selected data in JSON file
    records all tasks from all employees in a dictionary and stores
    as JSON data in a file
    """
    url_users = 'https://jsonplaceholder.typicode.com/users/'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    todo_data = requests.get(url_todos).json()
    new_dict = {}
    json_filename = 'todo_all_employees.json'

    for item in todo_data:
        id = str(item['userId'])
        if not new_dict.get(id):
            new_dict[id] = []
            user_data = requests.get(url_users + id).json()
        new_dict[id].append({"username": user_data['username'],
                             "task": item['title'],
                             "completed": item['completed']})

    with open(json_filename, 'w') as f:
        json.dump(new_dict, f)


if __name__ == '__main__':
    create_json()
