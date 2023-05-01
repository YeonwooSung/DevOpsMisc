# Kubernetes Service

In Kubernetes, a Service is a method for exposing a network application that is running as one or more Pods in your cluster.

## Table of Contents

- [What is a service?](#what-is-a-service)
- [Publishing Services (ServiceTypes)](#publishing-services-servicetypes)
    - [ClusterIP](#clusterip)
        - [What is ClusterIP?](#what-is-clusterip)
        - [How Service ClusterIPs are allocated?](#how-service-clusterips-are-allocated)
        - [How can you avoid Service ClusterIP conflicts?](#how-can-you-avoid-service-clusterip-conflicts)
    - [NodePort](#nodeport)

## What is a service?

A key aim of Services in Kubernetes is that you don't need to modify your existing application to use an unfamiliar service discovery mechanism.
You can run code in Pods, whether this is a code designed for a cloud-native world, or an older app you've containerized.
You use a Service to make that set of Pods available on the network so that clients can interact with it.

The Service API, part of Kubernetes, is an abstraction to help you expose groups of Pods over a network.
Each Service object defines a logical set of endpoints (usually these endpoints are Pods) along with a policy about how to make those pods accessible.

For example, consider a stateless image-processing backend which is running with 3 replicas.
Those replicas are fungible—frontends do not care which backend they use.
While the actual Pods that compose the backend set may change, the frontend clients should not need to be aware of that, nor should they need to keep track of the set of backends themselves.

The Service abstraction enables this decoupling.

The set of Pods targeted by a Service is usually determined by a selector that you define.
To learn about other ways to define Service endpoints, see Services without selectors.

If your workload speaks HTTP, you might choose to use an Ingress to control how web traffic reaches that workload.
Ingress is not a Service type, but it acts as the entry point for your cluster.
An Ingress lets you consolidate your routing rules into a single resource, so that you can expose multiple components of your workload, running separately in your cluster, behind a single listener.

The Gateway API for Kubernetes provides extra capabilities beyond Ingress and Service.
You can add Gateway to your cluster - it is a family of extension APIs, implemented using CustomResourceDefinitions - and then use these to configure access to network services that are running in your cluster.

## Publishing Services (ServiceTypes)

For some parts of your application (for example, frontends) you may want to expose a Service onto an external IP address, that's outside of your cluster.

Kubernetes ServiceTypes allow you to specify what kind of Service you want.

Type values and their behaviors are:

    - ClusterIP: Exposes the Service on a cluster-internal IP. Choosing this value makes the Service only reachable from within the cluster. This is the default that is used if you don't explicitly specify a type for a Service. You can expose the service to the public with an Ingress or the Gateway API.
    
    - NodePort: Exposes the Service on each Node's IP at a static port (the NodePort). To make the node port available, Kubernetes sets up a cluster IP address, the same as if you had requested a Service of type: ClusterIP.

    - LoadBalancer: Exposes the Service externally using a cloud provider's load balancer.

    - ExternalName: Maps the Service to the contents of the externalName field (e.g. foo.bar.example.com), by returning a CNAME record with its value. No proxying of any kind is set up.

### ClusterIP

ClusterIP is the default Kubernetes service. Your service will be exposed on a ClusterIP unless you manually define another type.

A ClusterIP provides network connectivity within your cluster.
It can’t normally be accessed from outside.
You use these services for internal networking between your workloads.

#### What is ClusterIP?

In Kubernetes, Services are an abstract way to expose an application running on a set of Pods. Services can have a cluster-scoped virtual IP address (using a Service of type: ClusterIP).
Clients can connect using that virtual IP address, and Kubernetes then load-balances traffic to that Service across the different backing Pods.

- [cluster ip service](./src/clusterip-service.yaml)

#### How Service ClusterIPs are allocated?

When Kubernetes needs to assign a virtual IP address for a Service, that assignment happens one of two ways:

    - dynamically:
        the cluster's control plane automatically picks a free IP address from within the configured IP range for type: ClusterIP Services.

    - statically:
        you specify an IP address of your choice, from within the configured IP range for Services.

Across your whole cluster, every Service `ClusterIP` must be unique. Trying to create a Service with a specific ClusterIP that has already been allocated will return an error.

#### Why do you need to reserve Service Cluster IPs?

Sometimes you may want to have Services running in well-known IP addresses, so other components and users in the cluster can use them.

The best example is the DNS Service for the cluster.
As a soft convention, some Kubernetes installers assign the 10th IP address from the Service IP range to the DNS service.
Assuming you configured your cluster with Service IP range 10.96.0.0/16 and you want your DNS Service IP to be 10.96.0.10, you'd have to create a Service like this:

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    k8s-app: kube-dns
    kubernetes.io/cluster-service: "true"
    kubernetes.io/name: CoreDNS
  name: kube-dns
  namespace: kube-system
spec:
  clusterIP: 10.96.0.10
  ports:
  - name: dns
    port: 53
    protocol: UDP
    targetPort: 53
  - name: dns-tcp
    port: 53
    protocol: TCP
    targetPort: 53
  selector:
    k8s-app: kube-dns
  type: ClusterIP
```

but as it was explained before, the IP address 10.96.0.10 has not been reserved; if other Services are created before or in parallel with dynamic allocation, there is a chance they can allocate this IP, hence, you will not be able to create the DNS Service because it will fail with a conflict error.

#### How can you avoid Service ClusterIP conflicts?

The allocation strategy implemented in Kubernetes to allocate ClusterIPs to Services reduces the risk of collision.

The ClusterIP range is divided, based on the formula min(max(16, cidrSize / 16), 256), described as never less than 16 or more than 256 with a graduated step between them.

Dynamic IP assignment uses the upper band by default, once this has been exhausted it will use the lower range.
This will allow users to use static allocations on the lower band with a low risk of collision.

### NodePort

A NodePort publicly exposes a service on a fixed port number.
It lets you access the service from outside your cluster.
You’ll need to use the cluster’s IP address and the NodePort number—e.g. 123.123.123.123:30000.

Creating a NodePort will open that port on every node in your cluster.
Kubernetes will automatically route port traffic to the service it’s linked to.

To make the node port available, Kubernetes sets up a cluster IP address, the same as if you had requested a Service of type: ClusterIP.

- [node port service](./src/nodeport-service.yaml)

## References

- [Kubernetes Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Kubernetes ClusterIP Allocations](https://kubernetes.io/docs/concepts/services-networking/cluster-ip-allocation/)
