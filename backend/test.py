import re

log = "Oct 27 07:22:19 reject lan IN=To_Fortinet OUT=eth1 SRC=10.10.40.1 DST=10.10.50.1 DPT=1001"  

# Define the regular expression pattern to match the fields
pattern = r'(\w{3}) (\d{1,2}) (\d{2}:\d{2}:\d{2}) (\w+) (\w+) IN=(\S+) OUT=(\S+) SRC=([\d.]+) DST=([\d.]+) DPT=(\d+)' 

# Use re.match to find the pattern in the log
match = re.match(pattern, log)

# Extract the fields 
if match:
    month = match.group(1)
    day = match.group(2)
    time = match.group(3)
    action = match.group(4)
    interface = match.group(5)
    inbound = match.group(6)
    outbound = match.group(7)
    source_ip = match.group(8)
    destination_ip = match.group(9)
    destination_port = match.group(10)

    # Print the extracted fields
    # print("Month:", month)
    # print("Day:", day)
    # print("time:", time)
    # print("Action:", action)
    # print("Interface:", interface)
    # print("Inbound:", inbound)
    # print("Outbound:", outbound)
    # print("Source IP:", source_ip)
    # print("Destination IP:", destination_ip)
    # print("Destination Port:", destination_port)
    
    json_parse = {"month": month,
                  "day": day,
                  "time": time,
                  "action": action,
                  "interface": interface,
                  "inbound": inbound, 
                  "outbound": outbound,
                  "source_ip": source_ip,
                  "destination_ip": destination_ip,
                  "destination_port": destination_port
                  }
    print (json_parse)

else:
    print("No match found.")
    
