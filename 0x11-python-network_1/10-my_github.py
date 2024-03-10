#!/usr/bin/python3
"""A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(response.json().get('id'))
