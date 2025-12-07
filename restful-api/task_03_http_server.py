#!/usr/bin/python3
'''
This file is about http server
'''

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import json

HOST = 'localhost'
PORT = 8000


class Service(BaseHTTPRequestHandler):
    '''this class is using HTTP do get'''

    def do_GET(self):
        if self.path == '/data':
            self.serve_json_data()
        elif self.path == "/status":
            self.status_printer()
        elif self.path == '/':
            self.main_page()
        elif self.path == "/info":
            self.info()
        else:
            self.error_handler()

    def main_page(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        self.wfile.write(bytes('<body>Hello, this is a simple API!</body>', 'utf-8'))

    def serve_json_data(self):
        data = {"name": "John", "age": 30, "city": "New York"}
        json_data = json.dumps(data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json_data, 'utf-8'))

    def status_printer(self):
        status_message = "OK" 
        self.send_response(200)
        self.send_header('Content-type', 'text/plain') 
        self.end_headers()
        self.wfile.write(bytes(status_message, 'utf-8'))

    def error_handler(self):
        error_message = f"Error: The requested resource {self.path} was not found."
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(bytes(error_message, 'utf-8'))

    def info(self):
        data = {"version": "1.0", "description": "A simple API built with http.server"}
        new_data = json.dumps(data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(new_data,'utf-8'))


server = HTTPServer((HOST, PORT), Service)
print("server is starting!")
server.serve_forever()
server.server_close()
print("Server stopped!")
