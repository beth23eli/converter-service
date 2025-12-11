# converter-service
This is a minimal FastAPI project that provides a units conversion feature. The project is containerized with Docker and deployed to Minikube.

## Features:
* Units conversion feature, ensuring the following requests:
    ```
        GET /api/conversion/km-to-miles/{value}
        GET /api/conversion/miles-to-km/{value}
        GET /api/conversion/celsius-to-fahrenheit/{value}
        GET /api/conversion/fahrenheit-to-celsius/{value}
    ```
* Health check endpoint:
    ```
        GET /health
    ```
* Configurable log level via environment variable (LOG_LEVEL); Log level managed at deployment time using a ConfigMap.
* Deployed in Kubernetes (Minikube)

## Project Structure

```
converter-service/
│── app/
│   ├── main.py
│   ├── __init__.py
│   ├── routers/
│   │   ├── conversion_router.py
│   │   └── health_router.py
│   ├── schemas/
│   │   └── conversion.py
│   ├── k8s/
│   │   ├── configmap.py
│   │   ├── deployment.py
│   │   ├── ingress.py
│   │   └── service.py
│── Dockerfile
│── README.md
└── ...
```


## Installation and Usage

In Linux, or your Linux vm, clone this repo anywhere you want and move into the directory:
```
git clone https://github.com/beth23eli/converter-service.git
cd converter-service
```

### Local Development
Ensure that you have installed uv-astral
1. Install dependencies using uv
    ```bash
    uv sync
    ```
2. Run locally
    ```bash
    uv run uvicorn app.main:create_app --reload --port 8000
    ```
3. Navigate to Swagger UI or test it yourself by making requests:
    ```
    http://localhost:8000/docs
    http://localhost:8000/api/conversion/km-to-miles/12
    ```

<br>

### Kubernetes Deployment
Ensure that you have installed minikube.
1. Start Minikube
    ```bash
    minikube start --driver=docker
    ```

2. Build Docker image
    ```bash
    minikube image build -t fastapi-img:latest .
    ```

3. Apply all configs:
    ```bash
    kubectl apply -f k8s/configmap.yaml
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    ```

4. Enable Minikube Ingress
    ```bash
    minikube addons enable ingress
    ```
    \
    Apply the Ingress
    ```bash
    kubectl apply -f k8s/ingress.yaml
    ```


5. Add /etc/hosts entry
    ```bash
    echo "$(minikube ip) converter.com" | sudo tee -a /etc/hosts
    ```

6. Test it:
    ```bash
    # in the browser
    http://converter.com/docs
    http://converter.com/health
    http://converter.com/api/conversion/km-to-miles/12

    # in the terminal
    curl http://converter.com/api/conversion/km-to-miles/12
    ```
<br>

#### Cleanup
```bash
kubectl delete -f ingress.yaml
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
kubectl delete -f configmap.yaml
```
<br><br>

### Important additions:
- Logging Configuration  
    - The service reads its log level from LOG_LEVEL that is configured via Kubernetes ConfigMap.
    - To update the log level:
        ```
        kubectl edit configmap fastapi-configmap
        kubectl rollout restart deployment fastapi-deployment
        ```
- uv-astral as Python package manager
    - It is a faster and more intuitive alternative to pip, venv, and pip-tools - all in one. Using uv, ensures that only necessary system dependencies are installed, focusing on reducing complexity and enhancing speed by syncing the dependencies based on a lock file.