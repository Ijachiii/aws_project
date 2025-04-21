# 🐳 AWS Django Project

This project is a containerized Django application deployed to AWS using Terraform. It supports background task processing with Celery and Redis and is fully Dockerized for local and production use.

---

## 🚀 Tech Stack

- **Backend:** Django (Python)
- **Task Queue:** Celery
- **Message Broker:** Redis
- **Containerization:** Docker, Docker Compose
- **Infrastructure:** AWS (EC2, ECR), Terraform

---

## 🧑‍💻 Local Development

### ✅ Prerequisites

- Docker
- Docker Compose
- Python 3.11+ (for local management commands, if needed)

### ⚙️ Setup

```bash
# Build and start the services
docker-compose build
docker-compose up
```

Once started, the Django app will be available at:
📍 http://localhost:8000 (or whichever port you mapped)

### Terraform Usage
terraform init
terraform apply -var="secret_key=your-django-secret-key" -auto-approve


✅ Features
	•	Background task processing via Celery + Redis
	•	Stateless, containerized architecture
	•	Infrastructure as code with Terraform
	•	Production-ready deployment using EC2 + ECR
	•	Clean separation of concerns across services
