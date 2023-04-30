# Replica Set in K8S

The `replica set` is the simplest way to manage multiple pods.
It is used to make sure that the specified number of pods are running.
It ensures that the specified number of pods are running by creating or deleting pods.

The replica set is a replacement for the replication controller.
The `replication controller` is using a simple equality-based selector, but the replica set is using various forms of selectors with `matchLabels` and `matchExpressions`.

It is recommended to use the replica set instead of the replication controller, in most cases.
