#!/usr/bin/python3
"""
A python script that uses REST API for a given employee Id and
returns info about the employee's to do list
"""
# Import the required modules
import json
import requests
import sys


if __name__ == "__main__":
    # Define the base url for the Api
    url = "https://jsonplaceholder.typicode.com/"

    # Check if the correct number of args is provided
    if len(sys.argv) != 2:
        print("Provide the Employee's id:")
        sys.exit(1)

        # Extract the employee's id from the command line
    employee_id = sys.argv[1]

    # Fetch user data from the API
    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()
    username = user.get("username")

    # Fetch todos for the employee
    params = {"userId": employee_id}
    todos_response = requests.get(url + "todos?userId={}".format(employee_id))
    todos = todos_response.json()

    data_to_export = {employee_id: []}

    for todo in todos:
        task_info = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        }
        data_to_export[employee_id].append(task_info)

    with open("{}.json".format(employee_id), "w",) as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)