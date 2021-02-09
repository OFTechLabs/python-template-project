********************
Deployment
********************
The REST API is deployed with the `FastAPI framework <https://fastapi.tiangolo.com/>`_ in Python. One of the main advantages of this framework is the automatic integration of `Swagger's UI documentation <https://swagger.io/tools/swagger-ui/>`_.

Installation
====================
Below you can find instructions for deploying the REST API either on your local machine or on Amazon AWS.

Locally
********************

* **Step 1**: Install Docker desktop

For testing locally on your own Windows or Mac PC we first need to have a Docker engine running.
For Linux users, Docker is natively available on your OS and you can skip step 1. Docker provides some excellent installation
instructions for `Windows <https://docs.docker.com/docker-for-windows/install/>`_ and
`Mac <https://docs.docker.com/docker-for-mac/install/>`_. After you've finished these installation guides, we'll continue
with step 2.

* **Step 2**: Syncronize this GitHub repository with a Docker hub repository, following `these instructions <https://docs.docker.com/docker-hub/builds/>`_. 

* **Step 3**: Run the Docker image in a container
To spin up a container based on the image in your DockerHub repository, open a command prompt or terminal window and use the following command: 

```bash
docker run -d -p 5000:8080 YourDockerHubAccountName/YourDockerHubRepository:latest
```

In order to spin up a locally built version, navigate to the directory containing "docker-compose.yml" and run:

```bash
docker-compose up --build
```

These commands retrieve the latest version of your application and will expose it at localhost:5000. The API swagger documentation should now be available at [http://localhost:5000/docs/](http://localhost:5000/docs/).

Amazon AWS
*********************
For instructions on how to deploy an app via REST API on Amazon Web Services, refer to the `template repository <https://github.com/OF-AVM-DK/ContainerizedAppDeployment>`_.


.. toctree::
   :maxdepth: 4
