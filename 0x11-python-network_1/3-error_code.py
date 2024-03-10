#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    import urllib.request as request
    import urllib.error as error
    from sys import argv

    try:
        url = request.Request(argv[1])
        with request.urlopen(url) as response:
            page = response.read().decode('utf-8')
            print(page)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
