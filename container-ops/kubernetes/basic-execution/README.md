# Execute application containers on the kubernetes cluster

- [Execute container with resource limits](./src/pod-with-resource-limits.yaml)
- [Execute container with command args](./src/pod-with-start-command.yaml)

## Execute pod with the init container

The `init container` is a container that will be executed before the main container. It is useful to execute some initialization tasks before the main container starts.

- [Execute pod with the init container](./src/pod-with-init-container.yml)
- [Execute pod with multiple init containers](./src/pod-with-multiple-init-containers.yaml)
