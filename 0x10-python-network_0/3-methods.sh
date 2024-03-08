#!/bin/bash
# A Bash script:
# 	- that sends a HEAD request to the URL stored in $1.
# 	- filters the output to only show the line that contains "Allow".
# 	- removes the first field (the word "Allow:"), and print line.
curl -sI "$1" | grep "Allow:" | cut -f2- -d' '
