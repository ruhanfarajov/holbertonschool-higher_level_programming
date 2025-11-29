#!/usr/bin/python3
'''this is doing america grreat again'''

import csv
import json


def convert_csv_to_json(filename):
    try:
        data = []

        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)

        with open(data.json, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data))

        return True
    except FileNotFoundError:
        return False

    except Exception:
        return False
