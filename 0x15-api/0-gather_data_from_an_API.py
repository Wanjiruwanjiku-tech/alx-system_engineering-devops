#!/usr/bin/python3
"""
A python script that uses REST API for a given employee Id and
returns info about the employee's to do list
"""
# Import the required modules
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

    # Fetch todos for the employee
    params = {"userId": employee_id}
    todos_response = requests.get(url + "todos?userId={}".format(employee_id))
    todos = todos_response.json()

    # Extract the completed tasks
    completed_tasks =[]

    for todo in todos:
        if todo.get("completed") is True:
            completed_tasks.append(todo.get("title"))
    
    # Dispay the information
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed_tasks), len(todos)))

    for completed_task in completed_tasks:
        print("\t {}".format(completed_task))