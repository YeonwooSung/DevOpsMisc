# DTrace

DTrace is a performance analysis and troubleshooting tool that is included by default with various operating systems, including Solaris, Mac OS X and FreeBSD. It is also available for Linux, but it is not included by default with most distributions.

The DTrace instruments all software.

Not just user-level software, including applications, databases and webservers, but also the operating system kernel and device drivers. The name is short for Dynamic Tracing: an instrumentation technique pioneered by DTrace which dynamically patches live running instructions with instrumentation code. The DTrace facility also supports Static Tracing: where user-friendly trace points are added to code and compiled-in before deployment.

DTrace provides a language, ‘D’, for writing DTrace scripts and one-liners. The language is like C and awk, and provides powerful ways to filter and summarize data in-kernel before passing to user-land. This is an important feature that enables DTrace to be used in performance-sensitive production environments, as it can greatly reduce the overhead of gathering and presenting data.
