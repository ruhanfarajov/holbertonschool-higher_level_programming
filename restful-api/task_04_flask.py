#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data_do():
    return jsonify(list(users))

@app.route("/status")
def suers():
    return "OK"

@app.route("/users/<username>")
def show_details(username):
    user = users.get(username.lower())
    if user:
        return jsonify(user), 200
    else:
        abort(404, description={"error": "User not found"})

@app.route("/add_user")
def add_user():
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({
        "message": "User added successfully",
        "user": data




if __name__ == "__main__":
    app.run()
