#!/usr/bin/python3
"""
    Returns information about an employee's TODO list progress.
    Requirements:
        Records all tasks that are owned by this employee
            Format: { "USER_ID": [
                {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
                {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
                "USER_ID": [
                {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
                {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]
            }
"""
import json
import requests
import sys


if __name__ == '__main__':
    # Base URL for the REST API
    api_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(sys.argv[1])

    user_response = requests.get(f'{api_url}/users/{employee_id}')
    todos_response = requests.get(f'{api_url}/todos?userId={employee_id}')

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print('Failed to fetch data from the API.')
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    with open('todo_all_employees.json', 'w') as f:
        json.dump({employee_id: [{
            'task': todo['title'],
            'completed': todo['completed'],
            'username': user_data['username']
        } for todo in todos_data]}, f)
