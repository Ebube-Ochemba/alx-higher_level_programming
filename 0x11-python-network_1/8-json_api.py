#!/usr/bin/python3
"""A Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    letter = argv[1] if len(argv) > 1 else ''

    try:
        response = requests.post('http://0.0.0.0:5000/search_user',
                                 data={'q': letter})
        json = response.json()
        if json:
            print('[{}] {}'.format(json['id'], json['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
