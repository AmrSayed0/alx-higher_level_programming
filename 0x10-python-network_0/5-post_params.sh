#!/bin/bash
# This script sends a POST request to a specified URL with data parameters and displays the body of the response.
# Use curl to send a POST request with data parameters (-d) and silence progress output (-s)
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
