#!/bin/bash
# display all HTTP methods the server will accept using curl.
curl -sI "$1" | grep -i "allow" | cut -d " " -f 2-
