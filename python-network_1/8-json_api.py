#!/usr/bin/python3
'''
Script that sends a POST request to a local server with a letter 'q' parameter,
and parses the JSON response to display user ID and name.
'''
import sys
import requests


def search_user_post():
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q_value = sys.argv[1]
    else:
        q_value = ""

    payload = {'q': q_value}

    try:
        response = requests.post(url, data=payload)

        try:
            json_data = response.json()

            if json_data and isinstance(json_data, dict):
                user_id = json_data.get('id')
                user_name = json_data.get('name')

                if user_id is not None and user_name is not None:
                    print(f"[{user_id}] {user_name}")
                else:
                    print("No result")

            elif json_data == {} or json_data == []:
                print("No result")

            else:
                print("No result")

        except requests.exceptions.JSONDecodeError:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}", file=sys.stderr)


if __name__ == "__main__":
    search_user_post()
