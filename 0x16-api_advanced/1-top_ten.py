#!/usr/bin/python3
""" sends get request to reddit api """
import requests


def top_ten(subreddit):
    """ call reddit api for subreddit and retrieve
    top ten posts for a subreddit """

    if type(subreddit) != str:
        raise TypeError("subreddit must be a string")

    url = 'http://reddit.com/r/' + subreddit + '/hot.json?limit=10'
    headers = {'User-Agent':
               'python3/Holberton_school_project/1.0 (by /u/karoline_dev)'}

    response = requests.get(url, headers=headers)
    try:
        body = response.json()
        top_posts_list = body['data']['children']
        for post in top_posts_list:
            print(post['data']['title'])
    except Exception:
        print('None')
