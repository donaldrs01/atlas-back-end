#!/usr/bin/python3
"""
Module to export all employee data into single JSON file
"""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f'{base_url}/users'
    todo_url = f'{base_url}/todos'
    file_name = 'todo_all_employees.json'

    #  Retreieve all emplopyee data
    employee_response = requests.get(employee_url)
    employees = employee_response.json()

    #  Retreive all todo list data
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    all_tasks = {}

    for employee in employees:
        user_id = employee['id']
        username = employee['username']
        #  create list to store tasks associated with current employee
        user_tasks = []
        for todo in todos:
            if todo['userId'] == user_id:
                task_info = {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                    }
                user_tasks.append(task_info)
                #  store all tasks associated with 1 employee in all_tasks dict
                all_tasks[user_id] = user_tasks

    with open(file_name, "w") as file:
        json.dump(all_tasks, file)
