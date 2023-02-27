#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import requests
import sys


def get_employee_todo_list(employee_id):
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id
    response = requests.get(url)
    todos = response.json()
    num_total_tasks = len(todos)
    completed_tasks = [todo.get('title') for todo in todos if todo.get('completed')]
    num_done_tasks = len(completed_tasks)
    url = 'https://jsonplaceholder.typicode.com/users/' + employee_id
    response = requests.get(url)
    employee = response.json()
    employee_name = employee.get('name')
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_done_tasks, num_total_tasks))
    for task_title in completed_tasks:
        print(f"\t {task_title}")


if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_employee_todo_list(employee_id)
