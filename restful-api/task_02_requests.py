#!/usr/bin/python3
'''
This is making america great again
'''
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url)
    status = response.status_code()
    if status == 200:
        dict_ = response.json()
        for i in dict_:
            print(dict_[i])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(url)
    status = response.status_code()
    if status == 200:
        dict_ = response.json
        with open('posts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["key", "value"])
            for key, value in dict_.items():
                writer.writerow([key, value])
