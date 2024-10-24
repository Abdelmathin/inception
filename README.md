# Inception

This project aims to deploy a complete web application using Docker containers. It involves setting up multiple services, including a WordPress application, a MariaDB database, an Nginx web server, and additional tools like Adminer, FTP, Redis, a Python server with SSH, and a static website. The project demonstrates how to manage various services in an isolated, scalable, and containerized environment using Docker Compose.

<p align="center">
  <img style="position: absolute;left:0%;top:0%;" height="auto" width="100%" src ="assets/inception.jpeg">
</p>

## Project Structure

The project consists of the following main components:

- **WordPress**: A content management system (CMS) running inside a Docker container for managing the website content.
- **MariaDB**: A lightweight, open-source relational database management system running in a separate container.
- **Nginx**: A web server that serves the WordPress application, acting as a reverse proxy to handle HTTP requests.
- **Adminer**: A simple and lightweight database management tool to interact with MariaDB.
- **FTP Server**: A containerized FTP server to handle file transfers.
- **Redis**: An in-memory data structure store used as a database, cache, and message broker.
- **Python Server with SSH**: A container running a Python server with SSH capabilities.
- **Static Website**: A simple static website served by Nginx.

## Features

- Fully containerized application using Docker.
- Scalable and easy-to-deploy infrastructure with Docker Compose.
- Services are isolated within their own containers, improving security and maintainability.
- Nginx acts as a reverse proxy to forward requests to various services.
- MariaDB stores and manages all WordPress data securely.
- Adminer provides an easy-to-use interface for managing MariaDB.
- FTP service for file transfers.
- Redis for caching and in-memory storage.
- Python server with SSH for remote access and execution.
- Nginx serves both WordPress and a static website.

## Getting Started

### Prerequisites

Ensure that the following software is installed on your system:

- **Docker**: [Get Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Get Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Abdelmathin/inception.git
    cd inception
    ```

2. Set up environment variables (optional):  
    You can configure the `.env` file with custom variables for the database, WordPress, Redis, FTP, or other services.

3. Build and start the Docker containers:
    ```bash
    docker-compose up --build
    ```

4. Access the services:

- **WordPress**:  
    ```
    http://localhost:443
    ```

- **Adminer**:  
    ```
    http://localhost:8080
    ```

- **FTP**: Use an FTP client to connect to:  
    ```
    ftp://localhost:21
    ```

- **Python Server with SSH**: SSH into the Python container:
    ```bash
    ssh user@localhost -p 2024
    ```

- **Static Website**:  
    ```
    http://localhost:8080
    ```

## Directory Structure

```markdown
srcs:
    ├── docker-compose.yml         # Main Docker Compose file defining all services
    └── requirements               # Folder containing configurations for all services

srcs/requirements:
    ├── bonus                      # Additional/Bonus services
    ├── mariadb                    # MariaDB database configuration
    ├── nginx                      # Nginx web server configuration
    └── wordpress                  # WordPress configuration

srcs/requirements/bonus:
    ├── adminer                    # Adminer (Database management tool) configuration
    ├── ftp                        # FTP server configuration
    ├── python-server-with-ssh     # Python server with SSH access
    ├── redis                      # Redis (in-memory data structure store) configuration
    └── static-website             # Static website configuration
```

# 🚀 Project Terminology

## 🌐 Docker
**Docker** is a powerful tool that enables you to package your applications and their dependencies into containers. These containers are portable and can run consistently across different environments.

### 🛠️ Example:
- After running the Docker command to start the container, you can access your application via `http://localhost`.

---

## 🎼 Docker Compose
**Docker Compose** is your orchestration maestro, allowing you to define and manage multi-container applications using a single configuration file (`docker-compose.yml`).

### 🎉 Example:
```bash
docker-compose up -d
```

With this command, you can start all the services defined in your `docker-compose.yml` file in detached mode, making it easy to manage complex applications.

## 🦸‍♂️ Containers

*Containers* are like mini virtual machines that isolate applications from their environments, ensuring they run consistently regardless of where they are deployed.

### 📊 Example:

```bash
docker ps
```

This command lists all running containers, helping you monitor your application’s state and resource usage.

## 👑 WordPress

*WordPress* is the king of content management systems (CMS), powering millions of websites worldwide. In this project, it is containerized for efficient deployment and scalability.

## 🦸‍♀️ MariaDB

*MariaDB* is an open-source relational database management system that serves as the backbone for WordPress, storing all your application data securely.

### 📄 Example:

```sql
CREATE DATABASE wordpress_db;
```

- This SQL command creates a new database specifically

## ⚙️ Adminer

*Adminer* is the friendly interface for database management. It’s like having a personal assistant for your MariaDB database, helping you navigate data effortlessly.

### 🔍 Example:

Access Adminer at `http://localhost:8080` to manage your databases and perform operations with ease. Data management has never been this straightforward!

## 🎨 Contribute & Engage

We welcome contributions from fellow developers! Whether you have ideas for improvements or want to report issues, your input is valuable. Join our community and let’s build something amazing together!
