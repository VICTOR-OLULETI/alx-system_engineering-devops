#!/usr/bin/python3
""" This script exports data in json format """
import csv
import json
import requests
import sys


if __name__ == "__main__":
    dict1 = {}
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    data = response.json()
    users = set([t['userId'] for t in data])
    for i in users:
        userid = str(i)
        url1 = 'https://jsonplaceholder.typicode.com/todos?userId=' + userid
        response = requests.get(url1)
        todos = response.json()
        url = 'https://jsonplaceholder.typicode.com/users/' + userid
        response = requests.get(url)
        employee = response.json()
        usernames = employee['username']
        temp_list = []
        temp_dict = {}
        for todo in todos:
            temp_dict["task"] = todo['title']
            temp_dict["completed"] = todo['completed']
            temp_dict["username"] = usernames
            temp_list.append(temp_dict)
        dict1[userid] = temp_list

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as f:
        json.dump(dict1, f)
