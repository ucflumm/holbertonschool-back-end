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

# Fetch user information for all users first
users_response = requests.get(f'{api_url}/users')
if users_response.status_code != 200:
    print('Failed to fetch user data from the API.')
    sys.exit(1)

users_data = users_response.json()
user_dict = {user['id']: user['username'] for user in users_data}

for todo in todos_data:
    user_id = todo['userId']
    task_info = {
        "username": user_dict.get(user_id, None),  # Use user_dict to get the username
        "task": todo['title'],
        "completed": todo['completed']
    }

    if user_id not in all_employee_tasks:
        all_employee_tasks[user_id] = []

    all_employee_tasks[user_id].append(task_info)

with open('todo_all_employees.json', 'w') as json_file:
    json.dump(all_employee_tasks, json_file, indent=4)
