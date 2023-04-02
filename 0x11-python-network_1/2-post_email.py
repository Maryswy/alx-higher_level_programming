#!/usr/bin/python3
from urllib import (request, parse)
from sys import argv

"""
script that takes in a url and an email, sends a POST request
to the url with the email as parameter and displays body of the
response
"""

if __name__ == "__main__":
    values = {}
    values["email"] = argv[2]
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()

    print(body.decode('utf8'))
