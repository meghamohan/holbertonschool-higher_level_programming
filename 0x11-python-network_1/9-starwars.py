#!/usr/bin/python3
"""
script that takes in a string and sends a search request to the Star Wars API
"""
import requests
import sys


if __name__ == "__main__":
    param = sys.argv[1]
    fullUrl = 'https://swapi.co/api/people/?search={}'.format(param)
    req = requests.get(fullUrl)
    jsonObj = req.json()
    print("Number of result: {}".format(jsonObj['count']))
    response = jsonObj['results']
    for person in response:
        print(person['name'])
