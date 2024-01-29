#!/usr/bin/python3
"""
A Script that, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    EMPLOYEE_NAME = employeeName.json()['name']

    totalTasks = 0

    for NUMBER_OF_DONE_TASKS in json_req:
        if NUMBER_OF_DONE_TASKS['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME, len(totalTasks), len(json_req)))

    for NUMBER_OF_DONE_TASKS in json_req:
        if NUMBER_OF_DONE_TASKS['completed']:
            print("\t {}".format(NUMBER_OF_DONE_TASKS.get('title')))
