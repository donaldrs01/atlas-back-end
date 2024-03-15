#!/usr/bin/python3
"""
Using an API, this script returns information about an employee's
TODO list based on their ID input
"""
import requests
import sys

def employee_todo_list(id):
    """Interacts with API and retrieves employee information based off ID"""

    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f'{base_url}/users/{id}'
    todo_url = f'{base_url}/todos'

    # store response object returned by GET request
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')




