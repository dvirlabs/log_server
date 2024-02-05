#!/bin/bash

# Filter log script
/root/log_server/backend/filter.sh &

# Python Backend
/root/log_server/backend/backend_python_script.sh &

wait
