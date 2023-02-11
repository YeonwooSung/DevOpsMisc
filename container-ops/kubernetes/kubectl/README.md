# kubectl

The `kubectl` is a command line interface for running commands against Kubernetes clusters.
The Kubernetes kubectl CLI allows one to communicate with Kubernetes clusters.
It can be mounted on any desktop or workstation, allowing us to remotely control our Kubernetes cluster.

## Table of Contents

* [Installation](#installation)
* [Scripts](#scripts)

## Installation

To install the `kubectl` follow the instructions in the corresponding documentation:

- [Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
- [MacOS](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)
- [windows](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/)

## Scripts

- Get pods
    - [Get all pods](./scripts/get_all_pods.sh)
    - [Get all pods with expanded output](./scripts/get_pods_with_expanded_outputs.sh)
    - [Get all pods with a given namespace](./scripts/get_all_pods_in_namespace.sh)
