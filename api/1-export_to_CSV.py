#!/usr/bin/python3
"""Module to export employee data into CSV file
"""
import csv
import requests
import sys


if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f'{base_url}/users/{sys.argv[1]}'
    #  Needed to filter tasks by user ID
    todo_url = f'{base_url}/todos?userId={sys.argv[1]}'
    file_name = f'{sys.argv[1]}.csv'

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    with open(file_name, "w", newline='') as file:
        csv_file = csv.writer(file)
        for todo in todos:
            csv_file.writerow([
                todo["userId"],
                employee_data["username"],
                todo["completed"],
                todo["title"]
                ])
