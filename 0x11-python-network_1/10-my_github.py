#!/usr/bin/python3
"""takes GitHub credentials and uses the GitHub API to display your id"""
import requests
import sys

def main():
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    auth = requests.auth.HTTPBasicAuth(username, password)

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        data = response.json()
        print(data['id'])
    except requests.exceptions.RequestException as err:
        print("Error: {}".format(err))

if __name__ == "__main__":
    main()
