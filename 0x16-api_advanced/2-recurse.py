#!/usr/bin/python3
""" sends get request to reddit api """
import requests


def recurse(subreddit, hot_list=[], after='1'):
    """ call reddit api recursively for subreddit and retrieve
    hot posts """

    headers = {'User-Agent':
               'python3/Holberton_school_project/1.0 (by /u/karoline_dev)'}

    if not after:
        return hot_list

    url = 'http://reddit.com/r/' + subreddit + \
        '/hot.json?limit=100&after=' + after
    try:
        response = requests.get(url, headers=headers)
        body = response.json()
        hot_list = hot_list + body['data']['children']
        return recurse(subreddit, hot_list, body['data']['after'])
    except Exception:
        return None
