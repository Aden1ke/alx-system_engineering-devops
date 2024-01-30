#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Specify the base URL of the REST API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a request to retrieve user details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # Make a request to retrieve user's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Extract relevant information
    employee_name = user_data.get('name', 'Unknown Employee')
    done_tasks = [task for task in todo_data if task['completed']]
    total_tasks = len(todo_data)

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({len(done_tasks)}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
