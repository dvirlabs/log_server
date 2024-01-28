#!/bin/bash

# Filter log script
/root/log_server/filter.sh &

# Insert logs to DB script
/root/log_server/insert_logs.sh &

# Python Backend
/root/log_server/backend_python_script.sh &

wait
