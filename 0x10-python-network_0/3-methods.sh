#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -sI -L $1  | grep "Allow" | cut -f2 -d ' '
