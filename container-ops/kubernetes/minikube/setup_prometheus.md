# Setup Prometheus on Minikube

## Prerequisites

Install Helm on Minikube master node:

```bash
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

## Part 1: Add Prometheus Helm repository

```bash
#
# add to helm chart
#

helm repo add stable https://charts.helm.sh/stable

helm repo add prometheus-community https://prometheus-community.github.io/helm-chart

#
# search repo
#
helm search repo prometheus-community
```

## Part 2: Install Prometheus

```bash
#
# Create namespace
#

kubectl create namespace prometheus

#
# Install kube-prometheus-stack
#

helm install stable prometheus-community/kube-prometheus-stack -n prometheus
```

## Part 3: Check Prometheus

```bash
kubectl get pods -n prometheus

kubectl get svc -n prometheus
```

## Part 4: Edit Services for access

In order to make prometheus and grafana available outside the cluster, use LoadBalancer or NodePort instead of ClusterIP.

### Edit Prometheus service

```bash
kubectl edit svc stable-kube-prometheus-sta-prometheus -n prometheus
```

In order to make prometheus available outside the cluster, use LoadBalancer or NodePort instead of ClusterIP.

```
  selector:
    app.kubernetes.io/name: prometheus
    operator.prometheus.io/name: stable-kube-prometheus-sta-prometheus
  sessionAffinity: None
  type: LoadBalancer
status:
  loadBalancer: {}
```

```bash
kubectl get svc -n prometheus
```

### Edit Grafana service

```bash
kubectl edit svc stable-grafana -n prometheus
```

In order to make grafana available outside the cluster, use LoadBalancer or NodePort instead of ClusterIP.

```
  selector:
    app.kubernetes.io/instance: stable
    app.kubernetes.io/name: grafana
  sessionAffinity: None
  type: LoadBalancer
status:
  loadBalancer: {}
```

```bash
kubectl get svc -n prometheus
```
