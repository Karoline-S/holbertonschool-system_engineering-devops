#!/usr/bin/python3
"""call a REST API and display formatted response"""

import csv
import requests
from sys import argv


def create_csv(id):
    """
    fetches data from REST API and saves in csv file
    """
    url_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos' \
        .format(id)

    user_data = requests.get(url_users).json()
    todo_data = requests.get(url_todos).json()
    user_id = str(id)
    user_name = user_data['username']
    filename = '{}.csv'.format(id)

    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

        for item in todo_data:
            task_status = str(item['completed'])
            task_title = item['title']
            row = [user_id, user_name, task_status, task_title]
            writer.writerow(row)


if __name__ == '__main__':
    create_csv(int(argv[1]))
