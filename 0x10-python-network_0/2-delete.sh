#!/bin/bash
# sends a DELETE request to the URL passed as the first argument
curl -s -L -X "DELETE" "$1"
