#!/usr/bin/python3
'''
this script gather some information about an employee
from an api and turns them into csv file
'''
import json
import requests


def main():
    '''this is the main function'''
    todos_url = (
            "https://jsonplaceholder.typicode.com/todos"
            )
    employee_url = (
            "https://jsonplaceholder.typicode.com/users"
            )

    response = requests.get(employee_url)
    users = response.json()
    data = {}
    for user in users:
        user_id = user['id']
        username = user['username']

        response = requests.get(todos_url, params={'userId': user_id})
        todos = response.json()

        tasks = []
        for todo in todos:
            tasks.append({
                'username': username,
                'task': todo['title'],
                'completed': todo['completed']
            })

        data[user_id] = tasks
    json_file = "todo_all_employees.json"
    with open(json_file, "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    main()
