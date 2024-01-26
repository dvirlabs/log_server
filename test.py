import subprocess
import re

original_logs = subprocess.getoutput('cat /var/log/fw_logs.log')
logs_line = original_logs.split('\n')

for log in logs_line:
    parts = re.split(r'\s', log)
    test_list = []
    
    parsed_logs_json = {
        "action": parts[0],
        "zone": f"{parts[1]} {parts[2]}",
        "srcint": parts[3],
        "destint": parts[4],
        "srcip": parts[5],
        "destip": parts[6],
        "destport": parts[8].split('=')[1]
    }
    
     
    print (parsed_logs_json)
    
    