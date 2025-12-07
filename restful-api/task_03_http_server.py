#!/usr/bin/python3
"""
Simple API using Python's http.server module.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status_code=200, content_type="text/plain"):
        """Helper to send headers."""
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests for various endpoints."""
        if self.path == "/":
            self._set_headers(200, "text/plain")
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._set_headers(200, "application/json")
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self._set_headers(200, "text/plain")
            self.wfile.write(b"OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._set_headers(200, "application/json")
            self.wfile.write(json.dumps(info).encode())

        else:
            # Handle unknown endpoints
            self._set_headers(404, "text/plain")
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    port = 8000
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
