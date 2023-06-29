#!/bin/bash
# This script sends a GET request to a specified URL with a custom header and displays the body of the response.
# Use curl to send a GET request with a custom header ("X-School-User-Id: 98") and silence progress output
curl -sH "X-School-User-Id: 98" "$1"
