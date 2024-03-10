#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status."""


if __name__ == '__main__':
    import requests

    response = requests.get('https://alx-intranet.hbtn.io/status')
    res = response.text
    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t- content: {res}")
