#!/bin/bash

while true
do
    curl -XPOST localhost:8001/update_db
    truncate -s 0 /var/log/fw_logs.log
    # sleep 10
done

