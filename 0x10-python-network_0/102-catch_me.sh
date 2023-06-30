#!/bin/bash
# Send a PUT request to the server with a custom header and data
curl -s -X PUT -H "Origin: You got me!" -d "user_id=98" 0.0.0.0:5000/catch_me

