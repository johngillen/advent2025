#!/bin/bash
# $1: day of month
# $2: command to run

while true; do
    if echo $(TZ='EST' date +'%d') | grep -q $1; then
        $2
        exit 0
    fi
    sleep 1
done
