#!/bin/bash

cd /root/log_server

source log_server/bin/activate

uvicorn main:app --host 0.0.0.0 --port 8001
