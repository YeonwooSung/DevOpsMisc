# Ingress

An Ingress is actually a completely different resource to a Service.
You normally use Ingresses in front of your Services to provide HTTP routing configuration.
They let you set up external URLs, domain-based virtual hosts, SSL, and load balancing.

Setting up Ingresses requires an Ingress Controller to exist in your cluster.
There’s a wide selection of controllers available.
Most major cloud providers have their own Ingress Controller that integrates with their load-balancing infrastructure.
[nginx-ingress](https://github.com/kubernetes/ingress-nginx/blob/main/README.md) is a popular standalone option that uses the NGINX web server as a reverse proxy to get traffic to your services.

You create Ingresses using the Ingress resource type.
The kubernetes.io/ingress.class annotation lets you indicate which kind of Ingress you’re creating.
This is useful if you’re running multiple cluster controllers.

- [Simple NGINX based Ingress](./src/nginx_ingress.yaml)

## Use ingress for serving multiple applications

Let's assume that we have 2 applications([service a](./src/service-a.yaml) and [service b](./src/service-b.yaml)) running in our cluster.

We could route each incoming request to corresponding service by using ingress based on predefined rules.

- [Ingress for specifing multiple services with paths](./src/ingress-no-host.yaml)
- [Ingress for host-based branching](./src/ingress-host-branching.yaml)
- [Ingress for SSL/TLS connection](./src/ingress-with-secret.yaml)

## References

- [Kubernetes Ingress Controllers](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)
