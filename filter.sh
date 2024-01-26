#!/bin/bash

source_file="/var/log/syslog"
destination_file="/var/log/fw_logs.log"

# Initial copy of the file
cp "$source_file" "$destination_file"

# Function to apply filters and copy the content
apply_filters_and_copy() {
    awk '/drop|accept|reject/ {print $7, $8, $9, $10, $11, $13, $14, $25, $23 }' "$source_file" \
    | sed 's/MAC=[^ ]*//' \
    | sed 's/LEN=[^ ]*//' \
    | sed 's/TOS=[^ ]*//' \
    | sed 's/PREC=[^ ]*//' \
    | sed 's/TTL=[^ ]*//' \
    | sed 's/RES=[^ ]*//' \
    | sed 's/WINDOW=[^ ]*//' \
    | sed 's/SPT=[^ ]*//' \
    | grep -v -E "succeeded|Exited|luci|connection|backgrounding" \
    > "$destination_file"
}

# Function to monitor file changes
monitor_file() {
    inotifywait -e modify -m "$source_file" |
    while read -r event; do
        echo "File changed. Updating filtered content..."
        apply_filters_and_copy
    done
}

# Run the initial copy and start monitoring
apply_filters_and_copy
monitor_file
