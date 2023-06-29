#!/bin/bash
# This script sends a JSON POST request to a specified URL with the contents of a JSON file and displays the body of the response.
# Use curl to send a POST request with the appropriate Content-Type header (-H "Content-Type: application/json"),
# and the JSON data from the specified file (-d "$(cat "$2")"), and silence progress output (-s)
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
