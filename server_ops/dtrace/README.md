# DTrace

DTrace is a performance analysis and troubleshooting tool that is included by default with various operating systems, including Solaris, Mac OS X and FreeBSD. It is also available for Linux, but it is not included by default with most distributions.

The DTrace instruments all software.

Not just user-level software, including applications, databases and webservers, but also the operating system kernel and device drivers. The name is short for Dynamic Tracing: an instrumentation technique pioneered by DTrace which dynamically patches live running instructions with instrumentation code. The DTrace facility also supports Static Tracing: where user-friendly trace points are added to code and compiled-in before deployment.

DTrace provides a language, ‘D’, for writing DTrace scripts and one-liners. The language is like C and awk, and provides powerful ways to filter and summarize data in-kernel before passing to user-land. This is an important feature that enables DTrace to be used in performance-sensitive production environments, as it can greatly reduce the overhead of gathering and presenting data.

## Provider

A provider represents a methodology for instrumenting the system. Providers make probes available to the DTrace framework. DTrace sends information to a provider regarding when to enable a probe. When an enabled probe fires, the provider transfers control to DTrace.

Providers are packaged as a set of kernel modules. Each module performs a particular kind of instrumentation to create probes. When you use DTrace, each provider has the ability to publish the probes it can provide to the DTrace framework. You can enable and bind tracing actions to any of the published probes.

Some providers have the capability to create new probes based on the user's tracing requests.

The usable providers are different for each operating system.
For example, you could have the following providers on Solaris:

- `syscall` : System calls
- `sched` : Scheduling
- `lockstat` : Lock contention
- `tcp` : TCP
- `udp` : UDP
- `file` : File I/O
- `proc` : Process creation and termination
- `pid` : Process level events monitoring - start, stop, exit, etc.
- `sysinfo` : System statistics
- `profile` : CPU profiling
- `fbt` : Kernel level dynamic tracing

## Probe

A probe has the following attributes:

- It is made available by a "provider"

- It identifies the "module" and the "function" that it instruments

- It has a "name"

These four attributes define a 4–tuple that serves as a unique identifier for each probe, in the format `provider:module:function:name`. Each probe also has a unique integer identifier.

## Predicate

Predicates are expressions that are enclosed in slashes / /. Predicates are evaluated at probe firing time to determine whether the associated actions should be executed. Predicates are the primary conditional construct used for building more complex control flow in a D program. You can omit the predicate section of the probe clause entirely for any probe. If the predicate section is omitted, the actions are always executed when the probe fires.

Predicate expressions can use any of the previously described D operators. Predicate expressions refer to D data objects such as variables and constants. The predicate expression must evaluate to a value of integer or pointer type. As with all D expressions, a zero value is interpreted as false and any non-zero value is interpreted as true.

## Action

Actions are user-programmable statements that the DTrace virtual machine executes within the kernel. Actions have the following properties:

- Actions are taken when a probe fires

- Actions are completely programmable in the D scripting language

- Most actions record a specified system state

- An action can change the state of the system in a precisely described way. Such actions are called destructive actions. Destructive actions are not allowed by default.

- Many actions use expressions in the D scripting language

## DTrace Built-in Variables

DTrace provides a number of built-in variables that are available to all D programs. These variables are used to access information about the current probe, the current process, and the current CPU.

- `arg0` to `arg9` : The first ten arguments to the current function
- `execname` : The name of the current executable process
- `pid` : The process ID of the current process that is running on the current CPU
- `uid` : The user ID of the current process that is running on the current CPU
- `timestamp` : The total time in nanoseconds since the system was booted
- `vtimestamp` : The total time in nanoseconds since the target thread had been loaded into the CPU
- `curthread` : The address of the current thread
- `probefunc` : Function part of the current probe (string)
- `probename` : Name part of the current probe (string)
- `curpsinfo` : The address of the current process's psinfo structure

You could find more built-in variables in [here](https://docs.oracle.com/cd/E18752_01/html/819-5488/gcfpz.html).
