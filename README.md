# Inception

**Inception** is a project that aims to deploy a complete web application using Docker containers. It involves setting up multiple services, including a WordPress application, a MariaDB database, an Nginx web server, along with additional tools like Adminer, FTP, Redis, a Python server with SSH, and a static website. This project demonstrates how to manage various services in an isolated, scalable, and containerized environment using Docker Compose.

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

<!--

# 42cursus-inception
This project aims to broaden your knowledge of system administration by using Docker. You will virtualize several Docker images, creating them in your new personal virtual machine.

<p align="center">
  <img style="position: absolute;left:0%;top:0%;" height="auto" width="100%" src ="assets/inception.jpeg">
</p>

```bash
git clone git@github.com:Abdelmathin/42cursus-inception.git
```

```bash
cd 42cursus-inception
```

```bash
make
```

# 💡 What is Docker?

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications.

# 💡 Docker Containers Vs Virtual Machines.
                                

### Docker Containers:
    
* Docker Containers contain binaries, libraries, and configuration files along with the application itself.
* They don’t contain a guest OS for each container and rely on the underlying OS kernel, which makes the containers lightweight.
* Containers share resources with other containers in the same host OS and provide OS-level process isolation.

### Virtual Machines:

* Virtual Machines (VMs) run on Hypervisors, which allow multiple Virtual Machines to run on a single machine along with its own operating system.
* Each VM has its own copy of an operating system along with the application and necessary binaries, which makes it significantly larger and it requires more resources.
* They provide Hardware-level process isolation and are slow to boot.

# 💡 Important Terminologies in Docker.

### Docker Image:

* It is a file, comprised of multiple layers, used to execute code in a Docker container.
* They are a set of instructions used to create docker containers.

## Docker Container:
* It is a runtime instance of an image.
* Allows developers to package applications with all parts needed such as libraries and other dependencies.

### Docker file:
* It is a text document that contains necessary commands which on execution helps assemble a Docker Image.
* Docker image is created using a Docker file.

### Docker Engine:

* The software that hosts the containers is named Docker Engine.
* Docker Engine is a client-server based application.
* The docker engine has 3 main components:
    * Server: It is responsible for creating and managing Docker images, containers, networks, and volumes on the Docker. It is referred to as a daemon process.
    * REST API: It specifies how the applications can interact with the Server and instructs it what to do.
    * Client: The Client is a docker command-line interface (CLI), that allows us to interact with Docker using the docker commands.

### Docker Hub:

* Docker Hub is the official online repository where you can find other Docker Images that are available for use.
* It makes it easy to find, manage, and share container images with others.

# 💡 Basic docker commands

* docker run:
    * This command creates and starts a new container based on a specified image.
    * For example, docker run hello-world will download and run the "hello-world" image.

* docker build:
    * This command builds a Docker image from a Dockerfile.
    * Example (builds an image with the tag "myapp" using the Dockerfile in the current directory.)
        ```bash
        docker build -t myapp . 
        ```

* docker pull:
    * This command downloads a Docker image from a registry.
    * For example, docker pull nginx will download the latest Nginx image from Docker Hub.

* docker ps:
    * This command lists all running containers.
    * Adding the -a flag (docker ps -a) will show all containers, including those that are stopped.

* docker stop:
    * This command stops a running container.
    * You can use either the container ID or name.
    * For example, docker stop mycontainer will stop the container named "mycontainer".

* docker rm:
    * This command removes a stopped container.
    * Like docker stop, you can use either the container ID or name.
    * For example, docker rm mycontainer will remove the container named "mycontainer".

-->