#!/usr/bin/python3
""" This script queries Reddit API """
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """ recurse temp, this function helps to perform the recursion
        Variables: subreddit - chosen subreddit by user input
                    hot_list - contains the list of the hot
                            posts of the subreddit
                    after - to check if there is more on another page
    """
    headers = {
        'User-Agent': 'vickey'
    }

    params = {
        'after': after
            }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(
        url, headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code != 200:
        return (None)

    response = response.json()
    posts = response['data']['children']

    for post in posts:
        title = post['data']['title']
        hot_list.append(title)
    after = response['data']['after']
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
