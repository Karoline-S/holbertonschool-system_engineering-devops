#!/usr/bin/python3
"""call a REST API and display formatted response"""

import csv
import requests
from sys import argv

try:
    if int(argv[1]):
        url_users = 'https://jsonplaceholder.typicode.com/users/{}' \
            .format(argv[1])
        url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos' \
            .format(argv[1])
except Exception:
    print('Usage: python3 0-gather_data_from_an_API.py <integer>')
    exit

user_data = requests.get(url_users).json()
todo_data = requests.get(url_todos).json()

user_id = str(user_data['id'])
user_name = user_data['username']
filename = '{}.csv'.format(argv[1])

with open(filename, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

    for item in todo_data:
        task_status = str(item['completed'])
        task_title = item['title']
        row = [user_id, user_name, task_status, task_title]
        writer.writerow(row)
