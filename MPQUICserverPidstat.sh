#!/bin/bash

target_command="target/debug/quiche-server --cert apps/src/bin/cert.crt --key apps/src/bin/cert.key --root apps/src/bin --listen 10.0.0.2:4433"
mkdir -p ./MPQUICstats
output_directory="./MPQUICstats"
file_count=$(find "$output_directory" -type f | wc -l)
echo "$file_count"

while true; do
  # Check if the process has started
  if pgrep -f "$target_command" >/dev/null; then
    # Get process statistics
    echo "Found targeted process with PID: $(pgrep -f "$target_command")"
    thePID=$(pgrep -f -n "$target_command")
    pidstat -p "$thePID"  1 >> ./MPQUICstats/serverPidstatOut_$file_count.log
    echo "Done recording pidstat"
    break
  fi
  sleep 1
done

