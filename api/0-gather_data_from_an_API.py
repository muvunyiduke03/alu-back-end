#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Get employee data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    employee_name = user_response.json().get("name")

    # Get TODOs
    todos_response =requests.get(todos_url)
    todos = todos_response.json()

    # filter completed tasks
    done_tasks = [task for task in todos if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)})")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
