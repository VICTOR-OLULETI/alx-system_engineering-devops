#!/usr/bin/python3
""" This module uses the REST API for a given employee ID
    returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    # employee id
    employee_id = sys.argv[1]
    # make the API request
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id
    response = requests.get(url)
    todos = response.json()
    # count the number of completed and total tasks
    num_total_tasks = len(todos)
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    num_done_tasks = len(completed_tasks)
    url = 'https://jsonplaceholder.typicode.com/users/' + employee_id
    response = requests.get(url)
    employee = response.json()
    employee_name = employee['name']
    # print the report
    print(f'Employee {employee_name} is done with tasks(
            {num_done_tasks}/{num_total_tasks}):')
    for task_title in completed_tasks:
        print(f"\t {task_title}")
