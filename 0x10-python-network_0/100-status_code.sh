#!/bin/bash
# script to get status code of response
curl -s -o /dev/null -I -w "%{http_code}" "$1"
