#!/usr/bin/python3
""" This script queries Reddit API """
import requests
import sys


def get_count(posts, word_list, counted):
    """ goes through the post response and counts the words
    based on the word list
    """
    if len(posts) > 0:
        post = posts[0]
        title = post['data']['title']
        for word in word_list:
            occur = [i.lower() for i in title.split()]
            word = word.lower()
            occurrence = len([w for w in occur if w == word])
            if occurrence:
                if counted.get(word):
                    counted[word] = counted[word] + occurrence
                else:
                    counted[word] = occurrence
        return (get_count(posts[1:], word_list, counted))
    return counted


def count_words(subreddit, word_list, after=None, counted={}, temp=0):
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
        'after': after,
        'limit': 100
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
    counted = get_count(posts, word_list, counted)
    after = response['data']['after']
    if after:
        count_words(subreddit, word_list, after, counted, temp)
    elif(counted == 0):
        print("")
        return (0)
    else:
        sorted_dict = dict(counted.items(), key=lambda x: x[1], reverse=True)
        for key, value in sorted_dict.items():
            if key not in ['key', 'reverse']:
                print("{}: {}".format(key, value))
    return (0)
