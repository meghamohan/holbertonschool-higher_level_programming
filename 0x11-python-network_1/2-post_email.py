#!/usr/bin/python3
"""

"""
import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    param = {'email': sys.argv[2]}
    encodedParam = urllib.parse.urlencode(param)
    encodedParam = encodedParam.encode('ascii')
    reqst = urllib.request.Request(url, encodedParam)
    with urllib.request.urlopen(reqst) as response:
        page = response.read()
    print(page.decode("utf8"))
