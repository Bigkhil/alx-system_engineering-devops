#!/usr/bin/python3
'''
this script gather some information about an employee
from an api and turns them into csv file
'''
import json
import requests
import sys


def main():
    '''this is the main function'''
    todos = (
            f"https://jsonplaceholder.typicode.com/todos/?userId={sys.argv[1]}"
            )
    employee_url = (
            f"https://jsonplaceholder.typicode.com/users/?id={sys.argv[1]}"
            )

    response = requests.get(todos)
    data = response.json()
    response = requests.get(employee_url)
    employee = response.json()
    username = employee[0].get('username')
    tasks = {sys.argv[1]: []}
    for todo in data:
        tasks[sys.argv[1]].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username,
            })
    json_name = f"{sys.argv[1]}.json"
    json_columns = [
            'task',
            'completed',
            'username',
            ]
    with open(json_name, "w") as jsonfile:
        json.dump(tasks, jsonfile)


if __name__ == "__main__":
    main()
