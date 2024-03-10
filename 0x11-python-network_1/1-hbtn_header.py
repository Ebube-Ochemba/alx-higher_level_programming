#!/usr/bin/python3
"""A Python script that kes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in
the header of the response"""


if __name__ == "__main__":
    import urllib.request as req
    from sys import argv

    url = req.Request(argv[1])
    with req.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
