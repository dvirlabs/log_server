#!/bin/bash

# Filter log script
/root/log_server/filter.sh &

# Python Backend
/root/log_server/backend_python_script.sh &

wait
