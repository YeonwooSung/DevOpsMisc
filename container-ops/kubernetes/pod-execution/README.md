# Execute Pod with application containers on the kubernetes cluster

- [Execute container with resource limits](./src/pod-with-resource-limits.yaml)
- [Execute container with command args](./src/pod-with-start-command.yaml)

## Execute pod with the init container

The `init container` is a container that will be executed before the main container. It is useful to execute some initialization tasks before the main container starts.

- [Execute pod with the init container](./src/pod-with-init-container.yml)
- [Execute pod with multiple init containers](./src/pod-with-multiple-init-containers.yaml)

## Execute pod with containers with various probes

There are 3 types of probes: `liveness probe`, `readiness probe`, and `startup probe`.

And there are 3 main methods to check the container: `HTTP GET`, `TCP Socket`, and `Exec`.

### liveness probe

The `liveness probe` is used to check if the container is alive. If the liveness probe fails, the container will be restarted.

- [Execute pod with liveness probe](./src/pod-with-liveness-probe.yaml)

By using liveness probe with `HTTP GET`, we could easily make a health check for the container.

- [Execute pod with liveness probe with HTTP GET for health check](./src/pod-with-get-probe.yaml)

### readiness probe

The `readiness probe` is used to check if the container is ready to receive traffic. If the readiness probe fails, the container will not receive traffic from the service.

By using the readiness probe, we can make sure that the container is ready to receive traffic.
For example, if the container is a web server, we can use the readiness probe to check if the web server is ready to receive traffic.

- [Execute pod with readiness probe](./src/pod-with-readiness-probe.yaml)

By using the readiness probe with `TCP Socket`, we could add 'ping' handler of the container for status checking.

- [Execute pod with readiness probe with TCP Socket for 'ping'](pod-with-tcp-probe.yaml)

### startup probe

The `startup probe` is exectued when the main container starts.

With the startup probe, we could set up the successThreshold and failureThreshold, which are threshold values for necessary consecutive successes or failures for the probe to be considered successful or failed for the startup probe.
By using the startup probe, we could prevent the container from being repeatedly restarted unstably.

- [Execute pod with startup probe](./src/pod-with-startup-probe.yaml)
