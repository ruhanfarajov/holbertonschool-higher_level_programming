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
        else:
            self.error_handler()

    def serve_json_data(self):
        data = {"name": "John", "age": 30, "city": "New York"}
        json_data = json.dumps(data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json_data, 'utf-8'))

    def status_printer(self):
        status_message = "<h2>OK</h2>"
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(status_message, 'utf-8'))

    def error_handler(self):
        error_message = f"<h3>Error: The requested resource {self.path} was not found.</h3>"
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(error_message, 'utf-8'))


server = HTTPServer((HOST, PORT), Service)
print("server is starting!")
server.serve_forever()
server.server_close()
print("Server stopped!")
