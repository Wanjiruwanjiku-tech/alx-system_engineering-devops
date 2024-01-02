#!/usr/bin/python3
"""
A python script that uses REST API for a given employee Id and
returns info about the employee's to do list
"""
# Import the required modules
import csv
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

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([employee_id, username, todo.get("completed"), todo.get("title")])