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
        return count_words(subreddit,
                           word_list,
                           hot_list,
                           body['data']['after'])
    except Exception as e:
        print(e)
        return None


def collate_and_print_results(word_list, hot_list):
    """ counts words in list of hot posts, adds to a dict and then prints
    results"""
    results_dict = {}

    word_list = [word.lower() for word in word_list]

    for post in hot_list:
        split_title = post['data']['title'].split()
        for word in word_list:
            for title_word in split_title:
                if word == title_word.lower():
                    results_dict[word] = results_dict.get(word, 0) + 1

    results_dict = dict(sorted(results_dict.items()))
    sorted_count = sorted(results_dict.items(),
                          key=lambda x: x[1],
                          reverse=True)
    for item in sorted_count:
        print('{}: {}'.format(item[0], item[1]))
