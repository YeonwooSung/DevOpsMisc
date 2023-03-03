#!/bin/bash

# Function to calculate CPU usage
calc_cpu_usage() {
    # Get the CPU usage percentage for each core
    usage=$(top -bn1 | grep '%Cpu' | awk '{print $2+$4}')

    # Calculate the average CPU usage
    num_cores=$(nproc)
    cpu_usage=$(echo "$usage / $num_cores" | bc)

    echo "$cpu_usage"
}

# Monitor RAM and CPU usage
while true; do
    # Get the total and used RAM
    ram_info=$(free -m | grep Mem)
    total_ram=$(echo $ram_info | awk '{print $2}')
    used_ram=$(echo $ram_info | awk '{print $3}')

    # Get the CPU usage
    cpu_usage=$(calc_cpu_usage)

    # Get the Disk usage
    disk_usage=$(df -h / | awk '/\// {print $(NF-1)}')

    # Get the Network usage
    network_rx_usage=$(ifconfig ens5 | grep 'RX' | grep 'byte' | awk '{print $5}' | cut -d ':' -f 2)
    network_tx_usage=$(ifconfig ens5 | grep 'TX' | grep 'byte' | awk '{print $5}' | cut -d ':' -f 2)

    # Print the RAM and CPU usage
    #echo "RAM usage: $used_ram MB / $total_ram MB    CPU usage: $cpu_usage%"

    echo "RAM: $used_ram MB / $total_ram MB"
    echo "CPU: $cpu_usage%"
    echo "Disk: $disk_usage"
    echo "Network RX: $network_rx_usage"
    echo "Network TX: $network_tx_usage"
    echo "-----------------------------"

    # Wait for 1 second before checking again
    sleep 1
done
