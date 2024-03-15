#!/usr/bin/python3
"""
Module to export employee data into JSON file
"""
import json
import requests
import sys


if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f'{base_url}/users/{sys.argv[1]}'
    #  Needed to filter tasks by user ID
    todo_url = f'{base_url}/todos?userId={sys.argv[1]}'
    file_name = f'{sys.argv[1]}.json'

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    tasks = []
    for todo in todos:
        task_info = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": employee_data["username"]
        }
        tasks.append(task_info)

    #  create dictionary where key = userID and value is list of tasks
    user_tasks_dict = {sys.argv[1]: tasks}

    with open(file_name, "w") as file:
        json.dump(user_tasks_dict, file)
