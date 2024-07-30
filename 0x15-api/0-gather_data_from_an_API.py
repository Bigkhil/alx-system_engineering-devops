#!/usr/bin/python3
# this script gather some information about an employee from an api
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
    url_notdone = (
            f"https://jsonplaceholder.typicode.com/todos/?userId={sys.argv[1]}"
            "&completed=false"
            )

    response = requests.get(todos)
    data = response.json()
    response = requests.get(url_notdone)
    no_notdone = len(response.json())
    response = requests.get(employee_url)
    employee = response.json()
    print(
            f"Employee {employee[0].get('name')} is done with tasks"
            f"({len(data) - no_notdone}/{len(data)}):"
            )
    for job in data:
        if job.get('completed') is True:
            print(f"\t{job.get('title')}")


if __name__ == "__main__":
    main()
