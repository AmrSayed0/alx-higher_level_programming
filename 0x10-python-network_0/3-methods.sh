#!/bin/bash
# This script sends a HEAD request to a specified URL and displays the HTTP methods the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
