import os
import datetime

# File to save logs
log_file = "uptime_log.txt"

# Get current date & time
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Detect OS and get uptime command
if os.name == "nt":  # Windows
    # systeminfo outputs system info; we'll log that a system check was made
    uptime_info = os.popen("net stats workstation").read()
    # Grab the line that usually contains the uptime
    for line in uptime_info.splitlines():
        if "Statistics since" in line:
            uptime_line = line.strip()
            break
else:  # Mac or Linux
    uptime_line = os.popen("uptime -p").read().strip()

# Combine timestamp with uptime info
log_entry = f"[{timestamp}] {uptime_line}\n"

# Append to log file
with open(log_file, "a") as file:
    file.write(log_entry)

print("Uptime logged:", log_entry)
