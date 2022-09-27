#!/usr/bin/python3
""" sends get request to reddit api """
import re
import requests


def count_words(subreddit, word_list, hot_list=[], after='1'):
    """ call reddit api recursively for subreddit and retrieve
    hot posts """

    headers = {'User-Agent':
               'python3/Holberton_school_project/1.0 (by /u/karoline_dev)'}

    if not after:
        collate_and_print_results(word_list, hot_list)
        return

    url = 'http://reddit.com/r/' + subreddit + \
        '/hot.json?limit=100&after=' + after
    try:
        response = requests.get(url, headers=headers)
        body = response.json()
        hot_list = hot_list + body['data']['children']
        return count_words(subreddit, word_list, hot_list, body['data']['after'])
    except Exception as e:
        print(e)
        return None


def collate_and_print_results(word_list, hot_list):
    """ counts words in list of hot posts, adds to a dict and then prints
    results"""
    results_dict = {}

    for post in hot_list:
        for word in word_list:
            if re.search(word, post['data']['title'], re.IGNORECASE):
                results_dict[word] = results_dict.get(word, 0) + 1

    sorted_count = sorted(results_dict.items(), key=lambda x:x[1], reverse=True)
    for i in sorted_count:
        print('{}: {}'.format(i[0], i[1]))
