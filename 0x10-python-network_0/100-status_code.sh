#!/bin/bash
# This script sends a request to a specified URL and displays only the status code of the response.
# Use curl to send a request, silence progress output (-s), redirect the response to null (-o /dev/null),
# and format the output to display only the HTTP status code (-w "%{http_code}")
curl -s -o /dev/null -w "%{http_code}" "$1"
