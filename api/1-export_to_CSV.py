#!/usr/bin/python3
""" Returns information about an employee's TODO list progress.
    Using what you did in the task #0,
    extend your Python script to export data in the CSV format.
"""
import csv
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

    with open(f'{employee_id}.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([employee_id,
                             user_data['username'],
                             todo['completed'],
                             todo['title']])
