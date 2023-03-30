#!/bin/bash
# Display the size of body of the response in bytes
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f 2
