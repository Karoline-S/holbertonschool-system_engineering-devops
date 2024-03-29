#!/usr/bin/python3
"""call a REST API and display formatted response"""

import requests
from sys import argv


def get_data(id):
    """
    fetches data from REST API and displays formatted response
    """
    url_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos' \
        .format(id)

    user_data = requests.get(url_users).json()
    todo_data = requests.get(url_todos).json()
    total_tasks = len(todo_data)
    completed_tasks = 0

    for item in todo_data:
        if item['completed']:
            completed_tasks += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(user_data['name'], completed_tasks, total_tasks))

    for item in todo_data:
        if item['completed']:
            print('\t {}'.format(item['title']))

if __name__ == '__main__':
    get_data(int(argv[1]))
