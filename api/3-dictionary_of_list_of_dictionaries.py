#!/usr/bin/python3
"""
    Returns information about an employee's TODO list progress.
"""
import json
import requests
import sys


api_url = "https://jsonplaceholder.typicode.com"

all_employee_tasks = {}

todos_response = requests.get(f'{api_url}/todos')

if todos_response.status_code != 200:
    print('Failed to fetch data from the API.')
    sys.exit(1)

todos_data = todos_response.json()

for todo in todos_data:
    user_id = todo['userId']
    task_info = {
        "username": None,
        "task": todo['title'],
        "completed": todo['completed']
    }

    if user_id not in all_employee_tasks:
        user_response = requests.get(f'{api_url}/users/{user_id}')
        if user_response.status_code == 200:
            user_data = user_response.json()
            task_info["username"] = user_data['username']
            all_employee_tasks[user_id] = []

    all_employee_tasks[user_id].append(task_info)

with open('todo_all_employees.json', 'w') as json_file:
    json.dump(all_employee_tasks, json_file, indent=4)
