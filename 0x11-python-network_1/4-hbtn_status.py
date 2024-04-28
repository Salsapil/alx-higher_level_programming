#!/usr/bin/python3
"""script that fetches a given url"""
import requests


def main():
    """main function"""
    url = "https://alx-intranet.hbtn.io/status"
    data = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(data.text)))
    print("\t- content: {}".format(data.text))


if __name__ == "__main__":
    main()
