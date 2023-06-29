#!/bin/bash
# Sends a request to a specified URL and retrieves the size of the response body
curl -s "$1" | wc -c
