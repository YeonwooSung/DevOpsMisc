# strace

[linux man page](https://manpages.ubuntu.com/manpages/trusty/man1/strace.1.html)

## -p : process id

Run strace for process with pid 653:

```bash
$ sudo strace -p 653
```

Run strace for 3 processes with pids 653, 654, and 658:

```bash
$ sudo strace -p 653 -p 654 -p 658
```

Run strace for multiple processes, and write output as a log file:

```bash
$ sudo strace -p 2916 -p 2929 -p 2930 -p 2931 -p 2932 -o /tmp/strace.log
```

## -c : Creating a Report

The -c (summary only) option causes strace to print a report. It generates a table for information about the system calls that were made by the traced program.

Run executable called "stex" with creating a report:

```bash
$ strace -c ./stex
```

The columns are:

- % time: The percentage of the execution time that was spent in each system call.
- seconds: The total time expressed in seconds and microseconds spent in each system call.
- usecs/call: The average time in microseconds spent in each system call.
- calls: The number of times that each system call was executed.
- errors: The number of failures for each system call.
- syscall: The name of the system call.

These values will show zeros for trivial programs that execute and terminate quickly.
Real-world values are shown for programs that do something more meaningful than our demonstration application.
