#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    reqst = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(reqst.text))
    print("\t- content:", reqst.text)
