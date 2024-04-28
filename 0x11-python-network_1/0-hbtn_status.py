#!/usr/bin/python3
# script that fetches a given url
from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        body = response.read()
    print("Body response:")
    print("\t- Type: {}".format(type(body)))
    print("\t- Content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
