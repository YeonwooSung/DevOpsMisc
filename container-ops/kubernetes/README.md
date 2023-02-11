# Kubernetes

K8s(Kubernetes) is a container orchestration system. It is a system for managing containerized applications across multiple hosts. It provides basic mechanisms for deployment, maintenance, and scaling of applications.

## Table of Contents

- [Pod](#pod)
- [Additional Resources](#additional-resources)

## Pod

tl;dr: A pod is a environment for running containers, not a container itself.

Pod is the smallest deployable unit of computing that can be created and managed in Kubernetes.
A Pod is a group of one or more containers, with shared storage/network, and a specification for how to run the containers.
Therefore, a Pod is a Kubernetes abstraction that represents a group of one or more application containers (such as Docker or rkt), and some shared resources for those containers.

This means that a Pod is a logical collection of containers that are treated as a single entity for management purposes.
So, when we deploy containers with Kubernetes, we deploy them as Pods, where each Pod contains one or more containers.

Containers in a Pod share an IP address and port space, and can find each other via localhost.
So, when deploying multiple containers in a Pod, we should take care of the port confliction.

Also, containers in a Pod share the same storage volume, so we can share files between containers in a Pod.

![Pods](./imgs/k8s_pod.png)

We could deploy one or more Pods in a single Node. And the entire Kubernetes cluster is composed of multiple Nodes.

![K8s cluster](./imgs/k8s_cluster.png)

## Additional Resources
