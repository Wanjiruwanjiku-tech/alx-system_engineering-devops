#!/usr/bin/python3
"""
A python script that uses REST API for a given employee Id and
returns info about the employee's to do list
"""
# Import the required modules
import json
import requests

def fetch_all_employee_data():
    """
    The function fetches data for all employees
    """
    # Define the base url for the Api
    url = "https://jsonplaceholder.typicode.com/"
    
    employees = requests.get(url + "users").json()
    data_to_export = {}

    for employee in employees:
        employee_id = employee["id"]
        
        todos_response = requests.get(url + "todos?userId={}".format(employee_id))
        todo_list = todos_response.json()
        data_to_export[employee_id] = []
        
        for todo in todo_list:
            task_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee.get("username")
                }
            data_to_export[employee_id].append(task_info)

    return data_to_export

if __name__ == "__main__":
    data_to_export = fetch_all_employee_data()
    name = 'todo_all_employees'
    with open("{}.json".format(name), "w",) as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)