#!/usr/bin/python3
""" This module uses the REST API for a given employee ID"""
import requests
import sys


def get_employee_todo_list(employee_id):
    """ This function accepts the employee_id and returns
        the employee information

        Args:
        employee_id (int): The ID of the employee.
        
        Returns:
        str: A string containing the employee TODO list progress
    """
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
    print(employee)
    employee_name = employee['name']
    username = employee['username']
    userid = employee['id']
    # print the report
    filename = '{}.json'.format(userid)
    with open(filename, 'w') as f:
        json.dump(todos, f)

if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_employee_todo_list(employee_id)
