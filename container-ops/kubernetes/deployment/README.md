# Deployment Control

The `deployment` is a Kubernetes object that allows us to deploy and update applications declaratively.

The main benefit of using a `deployment` is that it allows us to declare the procedure of `rollout`, which is the process of updating an application to a new version.
This means that it is possible to rollback to a previous version of the application if the new version is not working well.

- [deployment with 3 replicas, control update with RollingUpdate strategy](./src/deployment.yaml)

## Deploying with kubectl

1 - 0. scaling 'myapp-deployment' to 5 replicas

    ```bash
    $ kubectl scale deployment myapp-deployment --replicas=5
    ```

2 - 1. updating 'myapp-deployment' to the new version

    ```bash
    $ kubectl set image myapp-deployment nginx=nginx:1.9.1 --record
    ```

2 - 2. rolling back to the previous version

    ```bash
    $ kubectl rollout undo deployment myapp-deployment
    ```
