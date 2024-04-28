#!/usr/bin/python3
"""
list 10 commits of the repository with details passed as an argument.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    # GET request to GitHub API to retrieve commit info
    response = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))

    # Creating a 'list' from JSON response
    commits = response.json()

    # Iterating over the first 10 commits
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))


"""
Data PATH for the task
https://api.github.com/repos/rails/rails/commits
"""
