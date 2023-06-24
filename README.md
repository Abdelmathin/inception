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

