#!/bin/bash
# sending request to url and getting response
curl -sL 0:5000/catch_me -X PUT "You got me!" -H "Origin: X-School-User-Id" -d "user_id=98"
