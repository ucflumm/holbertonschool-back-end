#!/usr/bin/python3
"""Returns information about an employee's TODO list progress."""
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

    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Print the employee's name
    print(f"Employee {user_data['name']} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")
    # Print the title of completed tasks
    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")
