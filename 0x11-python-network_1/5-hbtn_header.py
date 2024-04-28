#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value"""
import sys
import requests


def main():
    url = sys.argv[1]
    with requests.get(url) as response:
        print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
