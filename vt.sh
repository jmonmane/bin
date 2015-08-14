#!/bin/bash

API_KEY="31aee15402b09192c5f0d9307edc2e6d2098ad5732b954bb12b4b6539caf39e2"
echo "Searches Virus Total DB for MD5 values"
# jsbrown, CCajigas
echo ""
#process file
IN=$(md5sum $1)
HASH=$(echo $IN | awk '{ print $1 }')
NAME=$(echo $IN | awk '{ print $2 }')

echo "Processing... $HASH"
REPLY=$(curl -s -X POST 'https://www.virustotal.com/vtapi/v2/file/report' --form apikey=$API_KEY --form resource="$HASH")
echo $REPLY | awk '{ print $1 }'
#|awk -F' ' '{print ([" "{$6$7}'|sed 's/["}]//g'

#process single hash
