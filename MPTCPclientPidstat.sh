#!/bin/bash

target_command="python3 client.py"
mkdir -p ./MPTCPstats
output_directory="./MPTCPstats"
file_count=$(find "$output_directory" -type f | wc -l)
#echo "test" > ./Pidstats/clientPidstatOut.log
echo "$file_count"

while true; do
  # Check if the process has started
  if pgrep -f "$target_command" >/dev/null; then
    # Get process statistics
    echo "Found targeted process with PID: $(pgrep -f "$target_command")"
    thePID=$(pgrep -f -n "$target_command")
    pidstat -p "$thePID"  1 >> ./MPTCPstats/clientPidstatOut_$file_count.log
    echo "Done recording pidstat"
    break
  fi
  sleep 1
done

