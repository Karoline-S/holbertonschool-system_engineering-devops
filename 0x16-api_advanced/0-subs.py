#!/usr/bin/python3
""" sends get request to reddit api """
import requests


def number_of_subscribers(subreddit):
    """ call reddit api for subreddit and retrieve
    number of subscribers from the response """

    if type(subreddit) != str:
        raise TypeError("subreddit must be a string")

    url = 'http://reddit.com/r/' + subreddit + '/about.json'
    headers = {'User-Agent':
               'python3/Holberton_school_project/1.0 (by /u/karoline_dev)'}

    response = requests.get(url, headers=headers)
    try:
        body = response.json()
        return body['data']['subscribers']
    except Exception:
        return 0
