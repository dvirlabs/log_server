#!/bin/bash

file_to_watch="/var/log/fw_logs.log"

echo "Watching for changes in $file_to_watch..."

while inotifywait -q -e modify -m "$file_to_watch"; do
    echo "File modified insert the logs to DB"
done