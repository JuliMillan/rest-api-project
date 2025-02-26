# REST APIs with Flask and Python course

In this repo I will be following along the course on REST API development.

The link to the course repo is https://github.com/tecladocode/rest-apis-flask-python/tree/develop



# Notes

### Docker
#### Kernel 
 - an operating system is made up of two main parts: the kernel and files/programs. 
 - It usually interacts with and controls the hardware. 
All linux distributions use the same linux kernel, and then they add different tools and applications, etc

You can run linux containers on mac or windows because that's how you'll deploy them in the cloud, through linux

Don't develop with different local containers and then deploy them to linux


To use linux containers locally we will use docker desktop. It creates a linux VM and run linux containers in that VM


A Docker container runs everything except the kernel. So all the applications, programs, etc. like bash, python, pip, etc

Docker containers are based on images which specify what is inside the container when it runs 

A docker image is a snapshop of source code, libraries, dependencies, tools and everything else (except OS kernel) that a containers needs to run

#### Dockerfile: 
- a definition of docker image
- We use them to build images
- We can then use an image to run more containers

#### Volumes: 
 - persistent data stores for containers. Mapping of a directory between your local file system and the container's file system.
 - Only for local development. When deploying, you don't use volumes. 


To run volumes on windows: ´docker run -dp 5000:5000 -w //app -v "%cd%://app" flask-smorest-api´

### Flask
#### Flask smorest
A blueprint is to divide an api into multiple segments


### SQLAlchemy
We add sqlalchemy and flask-sqlalchemy to the requirements, and pip install them in our local environment



