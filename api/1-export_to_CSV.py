#!/usr/bin/python3

import sys
import requests
import csv

if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f'{base_url}/users/{sys.argv[1]}'
    todo_url = f'{base_url}/todos'
    file_name = f'{sys.argv[1]}.csv'

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    with open(file_name, "w", newline='') as file:
        csv_file = csv.writer(file)
        csv_file.writerow([
            'USER_ID',
            'USERNAME',
            'TASK_COMPLETED_STATUS',
            'TASK_TITLE'
        ])
        for todo in todos:
            csv_file.writerow([
                todo['userId'],
                employee_data['name'],
                todo['completed'],
                todo['title']
                ])
