#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import sys
import requests


def main():
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    with requests.get(url, email) as response:
        print(response.text)


if __name__ == "__main__":
    main()
