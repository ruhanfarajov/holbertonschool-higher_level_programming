#!/usr/bin/python3
'''
This is making america great again
'''
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        print("Status Code: {}".format(response.status_code))
        data = response.json()
        for i in data:
            print(i['title'])
    else:
        print(f"Status Code: {response.status_code}")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        new_list = []
        for i in data:
            response ={
                'id': i.get('id'),
                'title': i.get('title'),
                'body': i.get('body')
            }
            new_list.append(response)
        
        with open('posts.csv', 'w', newline='', encoding='utf-8') as file:
            for i in new_list:
                writer = csv.DictWriter(file, fieldnames=['id', 'title','body'])
                writer.writeheader()
                writer.writerow(i)
    else:
        print(f"Status Code: {response.status_code}")
   
