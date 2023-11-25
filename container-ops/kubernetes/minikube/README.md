# minikube

The minikube is a tool that makes it easy to run Kubernetes locally.
Minikube runs a single-node Kubernetes cluster inside a VM on your laptop for users looking to try out Kubernetes or develop with it day-to-day.
It quickly sets up a local Kubernetes cluster on macOS, Linux, and Windows.

Run minikube on local machine with docker:
```bash
minikube start --container-runtime=docker --vm=true
```

## Table of Contents

* [Installation](#installation)
* [Scripts](#scripts)

## Installation

To install the minikube, please follow the instructions in the [official documentation](https://minikube.sigs.k8s.io/docs/start/).

## Scripts

- [Start minikube with Docker driver](./scripts/start_minikube_with_docker.sh)
- [Delete minikube server](./scripts/delete_minikube_server.sh)
