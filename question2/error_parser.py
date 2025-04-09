import re
import json

log_file_path = "/tmp/timestamp.log"
output_json_path = "/tmp/error_log.json"

# Regex to match error lines and extract timestamp and message
error_pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}).*?ERROR.*?-\s*(.*)")

errors = []

with open(log_file_path, "r") as file:
    for line in file:
        match = error_pattern.search(line)
        if match:
            timestamp, message = match.groups()
            errors.append({
                "timestamp": timestamp,
                "error_message": message.strip()
            })

# Write extracted data to JSON
with open(output_json_path, "w") as outfile:
    json.dump(errors, outfile, indent=4)

print(f"✅ Extracted {len(errors)} errors to {output_json_path}")
