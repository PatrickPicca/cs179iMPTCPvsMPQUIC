#!/bin/bash

target_command="python3 server.py"
mkdir -p ./MPTCPstats
output_directory="./MPTCPstats"
file_count=$(find "$output_directory" -type f | wc -l)
echo "$file_count"

while true; do
  # Check if the process has started
  if pgrep -f -n "$target_command" >/dev/null; then
    # Get process statistics
    echo "Found targeted process with PID: $(pgrep -f "$target_command")"
    thePID=$(pgrep -f -n "$target_command")
    echo "pidstat -p "$thePID" 1 >> ./MPTCPstats/serverPidstatOut_$file_count.log"
    pidstat -p "$thePID" 1 >> ./$output_directory/serverPidstatOut_$file_count.log
    #pidstat -p 31628 1 >> ./$output_directory/serverPidstatOut_$file_count.log
    echo "Done recording pidstat"
    break
  fi
  sleep 1
done