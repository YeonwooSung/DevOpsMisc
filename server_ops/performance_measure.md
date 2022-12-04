# Server performance measurement

## Overview

This document describes how to measure the performance of a server. Most of the commands in this document are for Linux.

## Table of Contents

- [Performance measurement](#performance-measurement)
    * [CPU](#cpu)
    * [Memory](#memory)
    * [Disk](#disk)
    * [Network](#network)
    * [References](#references)

## Performance measurement

### CPU

The CPU usage can be measured by using the `top` command.

```bash
$ top
```

### Memory

The memory usage can be measured by using the `free` command.

```bash
$ free -m
```

When you run the "free" command, the following output is displayed.

```bash
              total        used        free      shared  buff/cache   available
Mem:           1999         100        1798           0         100        1898
Swap:          2047           0        2047
```

The following is the description of each column.

- total: The total amount of memory.
- used: The amount of memory that is used.
- free: The amount of memory that is free.
- shared: The amount of memory that is shared.
- buff/cache: The amount of memory that is used as a buffer or cache.
- available: The amount of memory that is available without swapping.

Basically, the total amount of memory that the process can use is the sum of the "free", "buff/cache", and "available" columns.

### Disk

The disk usage can be measured by using the `df` command.

```bash
$ df -h
```

When you run the "df" command, the following output is displayed.

```bash
Filesystem      Size  Used Avail Use% Mounted on
udev            7.8G     0  7.8G   0% /dev
tmpfs           1.6G  1.3M  1.6G   1% /run
/dev/sda1        20G  3.3G   16G  18% /
tmpfs           7.8G     0  7.8G   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           7.8G     0  7.8G   0% /sys/fs/cgroup
/dev/loop0       56M   56M     0 100% /snap/core/7270
/dev/loop1       56M   56M     0 100% /snap/core/7396
/dev/loop2       56M   56M     0 100% /snap/core/7917
...
```

The following is the description of each column.

- Filesystem: The name of the file system.
- Size: The total size of the file system.
- Used: The amount of the file system that is used.
- Avail: The amount of the file system that is available.
- Use%: The percentage of the file system that is used.
- Mounted on: The mount point of the file system.

### Network

The network usage can be measured by using the `iftop` command.

```bash
$ iftop
```

## Performance measurement of a backend server

### wrk

The `wrk` command is a HTTP benchmarking tool.

```bash
# assume that the backend server is located at localhost with 8080 port

# generate 400 HTTP connections with 12 threads for 5 seconds
$ wrk -t 12 -c 400 -d 5 http://localhost:8080

# generate 10 HTTP connections for 5 seconds
$ wrk -c 10 -d 5 http://localhost:8080

# generate 10 HTTP connections for 5 seconds with detailed latency statistics
$ wrk -c 10 -d 5 --latency http://localhost:8080
```

The following is the description of each option.

* -t: The number of threads.
* -c: The number of connections.
* -d: The duration of the test.
* --latency: Measure latency with more detailed statistics.

### wrk2

The `wrk2` command is a HTTP benchmarking tool.

```bash
# assume that the backend server is located at localhost with 8080 port

# generate 400 HTTP connections with 12 threads for 5 seconds
$ wrk2 -t 12 -c 400 -d 5 http://localhost:8080

# generate 10 HTTP connections for 5 seconds
$ wrk2 -c 10 -d 5 http://localhost:8080

# generate 10 HTTP connections for 5 seconds with detailed latency statistics
$ wrk2 -c 10 -d 5 --latency http://localhost:8080
```

The following is the description of each option.

* -t: The number of threads.
* -c: The number of connections.
* -d: The duration of the test.
* --latency: Measure latency with more detailed statistics.
