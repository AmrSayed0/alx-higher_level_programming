#!/bin/bash
# This script makes a request to the endpoint 0.0.0.0:5000/catch_me and sends a PUT request with specific data and headers.
curl -s -X PUT -d "user_id=98" -H "Origin: You got me!" -L 0.0.0.0:5000/catch_me
