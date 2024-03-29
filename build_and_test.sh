#!/bin/bash

# Move api dir
cd ./api

#Build Docker Image with Compose
docker compose up -d

#Run Pytest
python3 -m pytest -v

#Health Check
health_status=$(curl http://localhost:8000/api/healthchecker)

if [[ $health_status == *"healthy"* ]]; then
    echo "API is healthy and Live!"
else
    echo "API is unhealthy..."
fi