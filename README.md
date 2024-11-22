# Traefik Reverse Proxy with Docker Compose and Ansible

This project sets up Traefik as a reverse proxy on a VPS using Docker Compose, managed and deployed with Ansible. It includes automatic SSL certificate management using Let's Encrypt.

## Features

    - Traefik Reverse Proxy: Manages incoming HTTP/HTTPS traffic.
    - Automatic SSL: Secure your connections with Let's Encrypt.
    - Docker Integration: Automatically discovers Docker services.
    - Web Dashboard: A UI for monitoring Traefik.

## Prerequisites

    - Docker and Docker Compose installed on the VPS.
    - Ansible installed on your local machine or CI/CD pipeline.

## Configuration Details

    - Entrypoints:
        - HTTP (:80)
        - HTTPS (:443)
        - TCP (:5432)
    - Let's Encrypt:
        - Managed by Traefik's certificatesresolvers.myresolver.
        - Certificates stored in ./data/traefik/acme.json.
    - Docker Integration:
        - Traefik listens to Docker events for automatic service discovery.