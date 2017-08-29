#!/usr/bin/python3
"""

"""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf8"))
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
