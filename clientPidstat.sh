#!/bin/bash

target_command="target/debug/quiche-client --no-verify https://10.0.0.2:4433/testVideo.mp4"
mkdir -p ./Pidstats
output_directory="./Pidstats"
file_count=$(find "$output_directory" -type f | wc -l)
#echo "test" > ./Pidstats/clientPidstatOut.log
echo "$file_count"

while true; do
  # Check if the process has started
  if pgrep -f "$target_command" >/dev/null; then
    # Get process statistics
    echo "Found targeted process with PID: $(pgrep -f "$target_command")"
    thePID=$(pgrep -f "$target_command")
    pidstat -p "$thePID"  1 >> ./Pidstats/clientPidstatOut_$file_count.log
    echo "Done recording pidstat"
    break
  fi
  sleep 1
done

