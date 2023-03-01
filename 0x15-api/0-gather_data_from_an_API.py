#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/'
    res = requests.get(user)
    json_o = res.json()
    for i in json_o:
        if i['id'] == int(employee_id):
            name = i['name']
    print("Employee {} is done with tasks".format(name), end="")

    todos = '{}todos?userId={}'.format(url, employee_id)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in l_task:
        print("\t {}".format(task.get("title")))
