#!/usr/bin/python3
"""displays the body of the response"""
import sys
import requests


def main():
    url = sys.argv[1]
    try:
        with requests.get(url) as response:
            response.raise_for_status()
            print(response.text)

    except:
        print("Error code: {}".format(response.status_code))


if __name__ == "__main__":
    main()
