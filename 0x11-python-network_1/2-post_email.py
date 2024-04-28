#!/usr/bin/python3
# sends a POST request to the passed URL with the email as a parameter
import sys
from urllib import request
from urllib import parse


def main():
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = parse.urlencode(email).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()
