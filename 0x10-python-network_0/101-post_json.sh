#!/bin/bash
# send a JSON POST request to URL, and displays the body of the response, using file as input
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
