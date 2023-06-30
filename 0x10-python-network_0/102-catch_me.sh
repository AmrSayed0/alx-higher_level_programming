#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me and retrieves the message "You got me!"
curl -s -X PUT -H "Origin: You got me!" -d "user_id=98" 0.0.0.0:5000/catch_me
