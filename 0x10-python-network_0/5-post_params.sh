#!/bin/bash
# takes in a URL, sends a POST request to the passed URL
curl -s -X -d "POST" "$1" "email=test@gmail.com&subject=I will always be here for PLD"
