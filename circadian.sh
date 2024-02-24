#!/usr/bin/env bash

curl -L -s "https://api.sunrise-sunset.org/json?lat=50.930581&lng=5.780691&formatted=0" \
  | jq '.results | "\(.sunrise) \(.sunset)"' | tr -d '"' \
  | awk -v now="$(date)" 'BEGIN {"date --date=$1"|getline a;"date --date=$2"|getline b;(now>=a&&now<=b)?r="OFF":r="ON";print r}'
