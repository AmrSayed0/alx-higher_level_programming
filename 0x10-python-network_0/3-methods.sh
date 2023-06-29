#!/bin/bash
# This script sends a HEAD request to a specified URL and displays the HTTP methods the server will accept.
# Use curl to send a HEAD request, retrieve the response headers, and filter for the "Allow" field
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
