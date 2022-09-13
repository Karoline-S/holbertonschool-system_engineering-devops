#!/usr/bin/python3
"""call a REST API and display formatted response"""

import json
import requests
from sys import argv


def create_json():
    """
    fetches data from REST API and stores selected data in JSON file
    """
    id = argv[1]
    url_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    user_data = requests.get(url_users).json()
    todo_data = requests.get(url_todos).json()
    new_dict = {id: []}

    for item in todo_data:
        if item['userId'] == int(id):
            new_dict[id].append({"task": item['title'],
                                 "completed": item['completed'],
                                 "username": user_data['username']})

    with open(id + '.json', 'w') as f:
        json.dump(new_dict, f)


if __name__ == '__main__':
    create_json()
