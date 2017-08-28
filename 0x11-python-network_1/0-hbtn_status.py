#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
    print("Body response:")
    print("\t- type:", type(page))
    print("\t- content:", page)
    print("\t- utf8 content:", page.decode("utf8"))
