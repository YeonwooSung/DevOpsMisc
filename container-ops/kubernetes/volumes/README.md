# Kubernetes Volumes

On-disk files in a container are ephemeral, which presents some problems for non-trivial applications when running in containers.
One problem occurs when a container crashes or is stopped.
Container state is not saved so all of the files that were created or modified during the lifetime of the container are lost.
During a crash, kubelet restarts the container with a clean state.
Another problem occurs when multiple containers are running in a Pod and need to share files.
It can be challenging to setup and access a shared filesystem across all of the containers.
The Kubernetes volume abstraction solves both of these problems.
Familiarity with Pods is suggested.

## Table of Contents

- [Types of Volumes](#types-of-volumes)
- [Pods with Volumes](#pods-with-volumes)
    - [Use AWS EBS for Volumes](#use-aws-ebs-for-volumes)
- [Persistent Volumes](#persistent-volumes)
    - [Persistent Volume Claim](#persistent-volume-claim)
    - [Persistent Volume wihtout Cloud Storage](#persistent-volume-wihtout-cloud-storage)

## Types of Volumes

Kubernetes supports several types of volumes.

- awsElasticBlockStore
- cephfs
- Configmap
- emptyDir
- hostPath
- local
- nfs
- persistentVolumeClaim
- rbd
- Secret

## Pods with Volumes

- [Pod with emptyDir](./src/pod-with-vol.yaml)
- [Pod with multiple containers and shared emptyDir](./src/pod-with-vol-and-multi-containers.yaml)

### Use AWS EBS for Volumes

We could use EBK(Elastic Block Storage) as a volume for a Pod.
To make this work, you need to add a awsElasticBlockStore key to the Pod's spec, and make the target EBS to be available in the same availability zone as the Pod.

The example code below provisions the EBS volume as a Volume automatically.
However, to use the existing provisioned EBS as a Volume, you need to use that EBS device as a PersistentVolume.

- [Pod with Elastic Block Storage as a volume](./src/pod-with-ebs.yaml)

## Persistent Volumes

A PersistentVolume (PV) is a piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using Storage Classes.
It is a resource in the cluster just like a node is a cluster resource.
PVs are volume plugins like Volumes, but have a lifecycle independent of any individual Pod that uses the PV.
This API object captures the details of the implementation of the storage, be that NFS, iSCSI, or a cloud-provider-specific storage system.

- [Simple example for Persistent Volume](./src/persistent-volume.yaml)
- [GP2 storage for Persistent Volume](./src/gp2-storageclass.yaml)

### Persistent Volume Claim

A PersistentVolumeClaim (PVC) is a request for storage by a user.
It is similar to a Pod.
Pods consume node resources and PVCs consume PV resources.
Pods can request specific levels of resources (CPU and Memory).
Claims can request specific size and access modes (e.g., they can be mounted ReadWriteOnce, ReadOnlyMany or ReadWriteMany, see AccessModes).

- [Simple example for Persistent Volume Claim](./src/pvc.yaml)

By running the `kubectl apply -f src/pvc.yaml` command, the PVC will be created and bound to the PV automatically.
After that, you can run the `kubectl apply -f src/pvc-with-attachment.yaml` command to create a Pod with the PV attached.

- [Pod with Persistent Volume Claim](./src/pvc-with-attachment.yaml)

The contents in the PV will be mounted to the `/data` directory in the Pod, however, the contents will not be deleted when the Pod is deleted.

### Persistent Volume wihtout Cloud Storage

If you are running K8S in on-premise environment, you may not have the cloud storage available.
In this case, `Rook` is a good option for you to use the local storage as a PV.

## References

- [Kubernetes Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)
- [Kubernetes Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
