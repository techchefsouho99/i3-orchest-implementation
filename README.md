# 🧠 I3 Orchest Implementation: Visual ML Pipelines for Movie Recommendations

This repository contains the setup, code, and supporting files for using [Orchest](https://www.orchest.io/) to build and run **visual machine learning pipelines** in the context of a **movie recommendation system**. The implementation supports:

- Collecting user ratings via simulated logs
- Cleaning and validating data
- Performing drift detection
- Orchestrating ML pipelines visually using Orchest

---

## 📌 Motivation

 The goal was to evaluate Orchest as an MLOps tool, experiment with it in a production-like scenario, and document its strengths and limitations in a blog post.

🔗 [Read the Blog Post →](#) _(https://medium.com/@tupaiadhikary/orchest-building-visual-ml-pipelines-in-the-real-world-d08d1b598803)_

---

## 🛠️ Tools Used

- **Orchest**: To visually build and run data pipelines in a web UI
- **Python (pandas, scipy)**: For data cleaning and drift detection
- **Minikube & Kubernetes**: Local K8s setup to self-host Orchest
- **GitHub**: For version control and public sharing

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/techchefsouho99/i3-orchest-implementation.git
cd i3-orchest-implementation
