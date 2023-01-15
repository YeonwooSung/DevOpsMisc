#!/bin/bash
# This script monitors CPU and memory usage

while :
do
    # Get the current usage of CPU, memory and disk
    MEMORY=$(free -m | awk 'NR==2{printf "%.2f%%\t\t", $3*100/$2 }')
    DISK=$(df -h | awk '$NF=="/"{printf "%s\t\t", $5}')
    CPU=$(top -bn1 | grep load | awk '{printf "%.2f%%\t\t\n", $(NF-2)}')

    # Print the usage
    echo "Memory Usage: $MEMORY"
    echo "Disk Usage: $DISK"
    echo "CPU Usage: $CPU"

    # Sleep for 2 seconds
    sleep 2
done
