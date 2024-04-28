#!/usr/bin/python3
"""search api"""
import sys
import requests


def main():
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        response = requests.post(url, data={'q': q})
        response.raise_for_status()

        data = response.json()
        if not data:
            print("No result")
        else:
            print(f"[{data['id']}] {data['name']}")

    except requests.exceptions.RequestException as err:
        print("Error: {}".format(err))
    except json.JSONDecodeError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
