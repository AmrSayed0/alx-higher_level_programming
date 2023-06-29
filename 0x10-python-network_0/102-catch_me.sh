#!/bin/bash
# This script makes a request to the endpoint 0.0.0.0:5000/catch_me and sends a PUT request with specific data and headers.
# Use curl to send a PUT request (-X PUT) to the specified endpoint (0.0.0.0:5000/catch_me),
# with data parameter (-d "user_id=98"), a custom Origin header (-H "Origin: You got me!"),
# and follow any redirects (-L), while silencing progress output (-s)
curl -s -X PUT -d "user_id=98" -H "Origin: You got me!" -L 0.0.0.0:5000/catch_me
