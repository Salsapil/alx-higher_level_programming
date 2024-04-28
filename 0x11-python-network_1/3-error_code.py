#!/usr/bin/python3
"""displays the body of the response"""
import sys
from urllib import request
from urllib import error


def main():
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))

    except error.HTTPError as err:
        print("Error code: {}".format(err.code))


if __name__ == "__main__":
    main()
