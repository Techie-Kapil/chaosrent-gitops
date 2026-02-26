# 🚀 GitOps Kubernetes Platform (K3s + Argo CD)

A self-healing, GitOps-driven Kubernetes platform built using K3s, Argo CD, and Kustomize.  
This project demonstrates modern DevOps deployment practices using Git as the single source of truth.

---

## 📌 Project Overview

This project simulates a production-style GitOps workflow where:

- Git is the single source of truth
- Argo CD continuously synchronizes cluster state
- Kubernetes ensures self-healing
- Kustomize manages environment-specific configurations
- Chaos testing validates resilience

The objective is to demonstrate real-world DevOps deployment automation and failure recovery mechanisms.

---

## 🖥️ Infrastructure Setup (Homelab Environment)

This platform was deployed and tested in a self-managed homelab environment rather than a local simulator.

Environment Details:
- K3s cluster running on local Linux server
- SSH-based remote cluster management
- Real network exposure via NodePort
- Persistent cluster state management
- Manual infrastructure provisioning and troubleshooting

This setup provided hands-on experience with real-world infrastructure challenges including networking, access management, and cluster debugging.

---

## 🏗️ Architecture

GitHub Repository  
↓  
Argo CD (GitOps Controller)  
↓  
K3s Kubernetes Cluster  
↓  
Application Deployments  

---

## 📂 Repository Structure

<img width="353" height="431" alt="image" src="https://github.com/user-attachments/assets/5c1c24ac-750d-4a04-84d0-1ed9f3c9f724" />

---


---

## ⚙️ Core Features

### GitOps Workflow
- Declarative Kubernetes manifests
- Argo CD Auto-Sync enabled
- Continuous drift detection and reconciliation
- Automated rollbacks

### Environment Management
- Kustomize bases and overlays
- Clean separation of base and production configurations

### Self-Healing Validation
- Kubernetes automatically recreates deleted pods
- Argo CD restores drifted resources

### Chaos Testing
- CronJob intentionally deletes application pods
- Automatic recovery verified through pod recreation and state reconciliation

---

## 🛠️ Setup & Installation

### 1️⃣ Install K3s

```bash
curl -sfL https://get.k3s.io | sh -
```

### 2️⃣ Install Argo CD

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

(📸 Add Screenshot Here -- TODO)

### 3️⃣ Deploy Applications via GitOps

```bash
kubectl apply -f argocd/app-demo-nginx.yaml
kubectl apply -f argocd/app-echo.yaml
kubectl apply -f argocd/app-chaos-killer.yaml
```

(📸 Add Screenshot Here -- TODO)

---

### 🔍 Validation Commands

Check pods:
```bash
kubectl get pods -n demo
```
Check services:
```bash
kubectl get svc -n demo
```

(📸 Add Screenshot Here -- TODO)

💥 Chaos Testing Validation

Verify CronJob:
```bash
kubectl get cronjobs -n demo
```

Observe:

- Pods get deleted
- Kubernetes recreates pods
- Argo CD remains in Synced state

(📸 Add Screenshot Here -- TODO)

### 🌐 Application Access

Application exposed via:

- NodePort
- Cluster DNS
- Optional remote access configuration

(📸 Add Screenshot Here -- TODO)

---

## 🔐 DevOps Best Practices Demonstrated

- Git as single source of truth
- No manual production edits
- Declarative infrastructure management
- Environment-specific configuration management
- Automated drift correction
- Failure simulation and recovery validation

## 📈 What This Project Proves

- Practical GitOps implementation
- Kubernetes self-healing capability
- Automated deployment pipelines
- Infrastructure resilience validation
- Real-world troubleshooting experience

## 🚀 Future Improvements

- Add Prometheus + Grafana monitoring
- CI pipeline for manifest validation
- Multi-node cluster setup
- Helm-based deployment
- Slack/Email alerting integration

--- 
## 👨‍💻 Author

Kapil






