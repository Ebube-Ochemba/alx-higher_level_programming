#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests


if __name__ == "__main__":

    response = requests.get("https://intranet.hbtn.io/status")
    res = response.text
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
