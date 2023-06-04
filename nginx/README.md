## NGINX

NGINX is open source software for web serving, reverse proxying, caching, load balancing, media streaming, and more.
It started out as a web server designed for maximum performance and stability.
In addition to its HTTP server capabilities, NGINX can also function as a proxy server for email (IMAP, POP3, and SMTP) and a reverse proxy and load balancer for HTTP, TCP, and UDP servers.

## Table of Contents

- [Why NGINX was created](#why-nginx-was-created)
- [NGINX Architecture](#nginx-architecture)

## Why NGINX was created

Igor Sysoev originally wrote NGINX to solve the [C10K](https://en.wikipedia.org/wiki/C10k_problem) problem, a term coined in 1999 to describe the difficulty that existing web servers experienced in handling large numbers (the 10K) of concurrent connections (the C).

Before NGINX, Apache HTTP server was most commonly used web server, which forks a new process for each incoming connection, and thus consumes significant system resources when handling large numbers of concurrent connections.
It keeps the connections open for a configurable amount of time, known as the keepalive timeout.
This approach worked well when web servers were used primarily to serve static content with reasonable number of concurrent connections.
However, as the web evolved, more and more dynamic content was generated, and the number of concurrent connections increased.
And when the number of concurrent connections exceeds 10,000, the web servers were faced with the C10K problem.

Basically, the system design of the Apache HTTP server was not suitable for the new web.
To overcome this issue, NGINX was designed to use an asynchronous, event‑driven approach to handling requests.

With its event‑driven, asynchronous architecture, NGINX revolutionized how servers operate in high‑performance contexts and became the fastest web server available.

## NGINX Architecture

The NGINX architecture consists of a master process and worker processes.
The master process reads and evaluates configuration, and maintains worker processes.
Worker processes do actual processing of requests.

Each worker process has event queue, which is used for queueing events that are to be processed by the worker process.
Here, an event is a type of notification that a process can receive from the operating system.
For example, when a new connection has been established, the "connection established" event is sent to the worker process, which will be queued in the event queue initailly.
When the connection is ready to be processed, the event is dequeued and processed by the worker process.
Events like "connection timeout" and "connection closed" are also queued and processed in the same way.

And, when the worker process processes the event, if the current event takes a long time to process (i.e. I/O polling, etc), the worker process register that task to it's `ThreadPool` and continue to process the next event in the event queue.
When the task is completed, the worker process will be notified by the `ThreadPool` and the worker process will process the next event in the event queue.
This asynchronous, event‑driven approach is the key to NGINX's ability to scale to large numbers of concurrent connections.
By doing this, NGINX can handle large numbers of concurrent connections with very light-weighted manner.

Due to it's asynchronous event-based approach, NGINX is not only used for Web Server or reverse proxy, it also widely used for load balancer, API gateway, etc.
It also has "HTTPS termination" feature, which lets many developers use NGINX as a HTTPS offloading server.
It also has "HTTP/2" support, and TCP/UDP offloading feature.

## Useful Links

- [Nginx HTTP server boilerplate configs](https://github.com/h5bp/server-configs-nginx)
