#!/bin/bash

# stop script on error
set -e

# run pub/sub sample app using certificates downloaded in package
printf "\nRunning pub/sub sample application...\n"
python3 temperaturePubSub.py -e a1zee5hib7fy9v-ats.iot.ap-northeast-1.amazonaws.com -r root-CA.crt -c raspberry_pi.cert.pem -k raspberry_pi.private.key -t raspberry_pi/log -acid 21082 -awk d59d7a22a068f15b