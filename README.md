# Nebula Notes — Flask + Redis (Docker Compose)

A minimal demo showing a Flask app connecting to Redis. Useful to demonstrate multi-container apps and Redis usage.

## Run locally with Docker Compose

Build and start services:
    docker compose up --build

Open:
    http://localhost:5000
Health:
    http://localhost:5000/health
Hits:
    http://localhost:5000/hits

Stop:
    docker compose down
