#!/bin/bash
# Makes a request to host:5000/catch_me that gets the message "You got me!"(very interesting) back and force.
curl -sL -H "Origin: School" -X PUT -d "user_id=98" aaccb40f696e.e0efb2d0.alx-cod.online:5000/catch_me
