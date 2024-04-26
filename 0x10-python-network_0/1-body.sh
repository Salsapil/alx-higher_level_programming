#!/bin/bash
# takes in a URL, sends a GET request to the URL
curl -s -L -X "GET" "$1"
