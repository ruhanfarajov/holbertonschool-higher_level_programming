#!/usr/bin/python3
'''
This is making america great again
'''
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for i in data:
            print(data[i])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open('posts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["key", "value"])
            for key, value in data.items():
                writer.writerow([key, value])
