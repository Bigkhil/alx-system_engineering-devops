#!/usr/bin/python3
'''
this script gather some information about an employee
from an api and turns them into csv file
'''
import csv
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
    tasks = []
    for todo in data:
        tasks.append({
            "USER_ID": sys.argv[1],
            "USERNAME": username,
            "TASK_COMPLETED_STATUS": todo.get('completed'),
            "TASK_TITLE": todo.get('title')
            })
    csv_name = f"{sys.argv[1]}.csv"
    csv_columns = [
            'USER_ID',
            'USERNAME',
            'TASK_COMPLETED_STATUS',
            'TASK_TITLE'
            ]
    with open(csv_name, "w", newline='') as csvfile:
        writer = csv.DictWriter(
                csvfile, fieldnames=csv_columns, quoting=csv.QUOTE_ALL
                )
        writer.writerows(tasks)


if __name__ == "__main__":
    main()
