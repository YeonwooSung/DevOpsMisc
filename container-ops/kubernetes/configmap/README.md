# ConfigMaps

A ConfigMap is an API object used to store non-confidential data in key-value pairs.
Pods can consume ConfigMaps as environment variables, command-line arguments, or as configuration files in a volume.

A ConfigMap allows you to decouple environment-specific configuration from your container images, so that your applications are easily portable.

Be careful to not to store sensitive information in ConfigMaps, such as ssh keys or secret keys.

## Table of Contents

* [Motivations](#motivations)
* [Create ConfigMaps](#create-configmaps)
    * [Create a ConfigMap from text values](#create-a-configmap-from-text-values)
    * [Create a ConfigMap from a file](#create-a-configmap-from-a-file)
    * [Create a ConfigMap from an env file](#create-a-configmap-from-an-env-file)
* [Mount ConfigMaps](#mount-configmaps)
    * [Mount the ConfigMap as a volume](#mount-the-configmap-as-a-volume)
    * [Mount the ConfigMap as an environment variable](#mount-the-configmap-as-an-environment-variable)
* [Difference between ConfigMap and Secret](#difference-between-configmap-and-secret)

## Motivations

Use a ConfigMap for setting configuration data separately from application code.

For example, imagine that you are developing an application that you can run on your own computer (for development) and in the cloud (to handle real traffic).
You write the code to look in an environment variable named DATABASE_HOST.
Locally, you set that variable to localhost.
In the cloud, you set it to refer to a Kubernetes Service that exposes the database component to your cluster.
This lets you fetch a container image running in the cloud and debug the exact same code locally if needed.

A ConfigMap is not designed to hold large chunks of data.
The data stored in a ConfigMap cannot exceed 1 MiB.
If you need to store settings that are larger than this limit, you may want to consider mounting a volume or use a separate database or file service.

## Create ConfigMaps

### Create a ConfigMap from text values

We could create a ConfigMap from text values:

```bash
$ kubectl create configmap my-config --from-literal=mycategory.mykey=myvalue --from-literal=mycategory.mykey2=myvalue2
```

The command above will create a ConfigMap named `my-config` with two key-value pairs.
To print out the created ConfigMap, we could use the following command:

```bash
$ kubectl get configmap my-config -o yaml
```

The above command will print out the ConfigMap in YAML format:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: myapp-config
  namespace: default
data:
  mycategory.mykey: myvalue
  mycategory.mykey2: myvalue2
```

### Create a ConfigMap from a file

Let's assume that the `myconfig.properties` file contains the following content:

```properties
myconfigid=1125
publicapikey=i38ahsjh2
```

We could create a ConfigMap from a file 'myconfig.properties' by running the following command:

```bash
$ kubectl create configmap my-config --from-file=myconfig.properties
```

Then, we could check whether the ConfigMap is created successfully by running `kubectl describe` command:

```bash
$ kubectl describe configmaps my-config
```

### Create a ConfigMap from an env file

Let's assume that the `myconfig.env` file contains the following content:

```properties
myconfigid=1125
publicapikey=i38ahsjh2
```

We could create a ConfigMap from an env file 'myconfig.env' by running the following command:

```bash
$ kubectl create configmap my-config --from-env-file=myconfig.env
```

Then, we could check whether the ConfigMap is created successfully by running `kubectl describe` command:

```bash
$ kubectl describe configmaps my-config
```

## Mount ConfigMaps

### Mount the ConfigMap as a volume

To use the ConfigMap data in a volume in a Pod, we need to mount the ConfigMap as a volume.
To achieve this, we need to add a `volumes` section in the Pod spec, and add a `volumeMounts` section in the container spec.

- [Example Pod spec for mouning configmap as a volume](./src/pod-mounting-cm.yaml)

### Mount the ConfigMap as an environment variable

We could also mount the ConfigMap as an environment variable in a Pod.

- [Example Pod spec for mouning configmap as an environment variable](./src/pod-mounting-cm-as-env.yaml)

## Difference between ConfigMap and Secret

ConfigMaps are similar to Secrets, but designed to more conveniently support working with strings that do not contain sensitive information.

The Secret API resource lets you store and manage sensitive information, such as passwords, OAuth tokens, and ssh keys.
The Secret API resource encodes the data as base64 strings, whereas the ConfigMap API resource does not encode the data.

To use the Secret in a Pod, you should also mount the Secret (either as a volume or as individual environment variables) in addition to referencing it from a container in the Pod spec.

- [Example Pod spec for mouning secret as a volume](./src/pod-mounting-secret.yaml)
- [Example Pod spec for mouning secret as an environment variable](./src/pod-mounting-secret-as-env.yaml)

## References

- [K8S: ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)
- [K8S: Secret](https://kubernetes.io/docs/concepts/configuration/secret/)
