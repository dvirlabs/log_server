import uvicorn
from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import FileResponse
import subprocess
from pymongo import MongoClient
import json
import re

app = FastAPI()

filter = "(\w+)\s(.*):\sIN=(\w+)\sOUT=(\w+)\sSRC=(.*)\sDST=(.*)\s\sDPT=(\d+)"

# The original file of the logs
log_directory = "/var/log/syslog"

# Connect to MongoDB
client = MongoClient('mongodb://192.168.1.60:27017/openwrt')
db = client['openwrt']
collection = db['fw_logs']

@app.get("/")
async def read_root():
    return {"message": "Welcome to the log server. Use /logs/{filename} to view log files."}


@app.get("/fw_logs")
async def get_fw_logs() -> list:
    original_logs = subprocess.getoutput('cat /var/log/fw_logs.log')
    logs_line = original_logs.split('\n')
    logs_json = []
    for log in logs_line:
        action, zone, srcint, destint, srcip, destip, destport = re.findall(filter, log)[0]
        parsed_logs_json = {
            "action": action,
            "zone": zone,
            "srcint": srcint,
            "destint": destint,
            "srcip": srcip,
            "destip": destip,
            "destport": destport
        }
        logs_json.append(parsed_logs_json)
    return logs_json
        
        
        

           

# @app.post("/update_db")
# async def insert_logs_to_db():
#     original_logs = subprocess.getoutput('cat /var/log/fw_logs.log')
#     logs_line = original_logs.split('\n')
#     logs_json = []
#     for log in logs_line:
#         action, zone, srcint, destint, srcip, destip, destport = re.findall(filter, log)[0]
#         parsed_logs_json = {
#             "action": action,
#             "zone": zone,
#             "srcint": srcint,
#             "destint": destint,
#             "srcip": srcip,
#             "destip": destip,
#             "destport": destport
#         }
#         logs_json.append(parsed_logs_json)
#     collection.insert_many(logs_json)
        
#     return "DB update successfuly"
            
        
        

# @app.get("/logs/{filename}")
# async def read_log(filename: str):
#     log_path = Path(log_directory) / filename

#     if not log_path.is_file():
#         raise HTTPException(status_code=404, detail="Log file not found")

#     return FileResponse(log_path)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", workers=1, port=8001, reload=True, access_log=False)
   