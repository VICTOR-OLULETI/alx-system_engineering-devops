#!/usr/bin/python3
""" This script exports data in json format """
import csv
import json
import requests
import sys


def get_employee_todo_list(employee_id):
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id
    response = requests.get(url)
    todos = response.json()
    # print(todos)
    num_total_tasks = len(todos)
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    num_done_tasks = len(completed_tasks)
    url = 'https://jsonplaceholder.typicode.com/users/' + employee_id
    response = requests.get(url)
    employee = response.json()
    employee_name = employee['name']
    userid = str(todos[0]['userId'])
    usernames = employee['username']
    dict1 = {}
    temp_list = []
    temp_dict = {}
    for todo in todos:
        temp_dict["task"] = todo['title']
        temp_dict["completed"] = todo['completed']
        temp_dict["username"] = usernames
        temp_list.append(temp_dict)
    dict1[userid] = temp_list

    filename = '{}.json'.format(userid)
    with open(filename, 'w') as f:
        json.dump(dict1, f)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_employee_todo_list(employee_id)
