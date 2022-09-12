#!/usr/bin/python3
"""call a REST API and display formatted response"""

import requests
from sys import argv

try:
    if int(argv[1]):
        url_users = 'https://jsonplaceholder.typicode.com/users/{}' \
            .format(argv[1])
        url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos' \
            .format(argv[1])
except as Exception:
    print('Usage: python3 0-gather_data_from_an_API.py <integer>')
    exit

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
        print('\t{}'.format(item['title']))
