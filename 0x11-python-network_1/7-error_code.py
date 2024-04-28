#!/usr/bin/python3
"""displays the body of the response"""
import sys
import requests
from urllib import error


def main():
    url = sys.argv[1]
    try:
        with requests.post(url) as response:
            response.raise_for_status()
            print(response.text)

    except error.HTTPError as err:
        print("Error code: {}".format(response.status_code))


if __name__ == "__main__":
    main()
