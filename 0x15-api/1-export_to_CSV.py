#!/usr/bin/python3
""" This module exports data in the CSV format """
import csv
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
    employee_name = employee['name']
    username = employee['username']
    userid = todos[0]['userId']
    filename = '{}.csv'.format(userid)
    # print the report
    with open(filename, mode='w+', newline="") as f:
        # create a writer object
        writer = csv.writer(f,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)

        # Write the data rows
        # userId,id,title,completed
        for row in todos:
            temp = []
            user_id = row.get("userId")
            user_title = row.get("title")
            completed = row.get("completed")
            temp.append(user_id)
            temp.append(username)
            temp.append(completed)
            temp.append(user_title)
            writer.writerow(temp)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_employee_todo_list(employee_id)
    print("Data written to output.csv")
