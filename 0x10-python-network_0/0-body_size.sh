#!/bin/bash
# script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
# curl -sI "$1" | grep "Content-Length" | cut -d: -f2 | cut -d ' ' -f2
curl -sI "$1" | grep "Content-Length" | rev | cut -d ' ' -f 1 | rev
