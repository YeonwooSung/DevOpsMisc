# Kind

[kind](https://github.com/kubernetes-sigs/kind): Kubernetes IN Docker - local clusters for testing Kubernetes

## Create cluster

You could easily create a cluster with `kind create cluster`:

```bash
sudo kind create cluster --name mykind --config - <<EOF
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  disableDefaultCNI: true   # do not install kindnet
  kubeProxyMode: none       # do not run kube-proxy
nodes:
- role: control-plane
- role: worker
- role: worker
- role: worker
EOF
```

Alternatively, you could create a cluster with `kind create cluster --config=-`:

```
cat <<EOF | kind create cluster --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
EOF
```
