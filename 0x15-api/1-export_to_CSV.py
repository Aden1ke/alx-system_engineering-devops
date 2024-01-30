#!/usr/bin/python3
"""extending Python script to export data in the CSV format."""

import csv
import requests
from sys import argv as av


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users/"

    user_data = requests.get(base_url + "{}".format(av[1])).json()
    todo_data = requests.get(base_url + "{}/todos".format(av[1])).json()

    with open("{}.csv".format(av[1]), mode="w") as file:
        writer = csv.writer(file, delimiter=",", quotechar="\"",
                            quoting=csv.QUOTE_ALL)

        for todo in todo_data:
            row = [
                    user_data.get("id"),
                    user_data.get("username"),
                    todo.get("completed"),
                    todo.get("title")
                    ]
            writer.writerow(row)
