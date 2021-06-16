![Build Status](https://github.com/OF-AVM-DK/ContainerizedAppDeployment/workflows/sphinx-autobuild/badge.svg)
![Build Status](https://github.com/OF-AVM-DK/ContainerizedAppDeployment/workflows/app-tests/badge.svg)

# Containerized app deployment
This repository serves as a template to host your Python application in a Docker container as a microservice that can be accessed by REST API. 

## Structure
The folder structure for this project is as follows:

    .
    ├── .github                 # Github specific files (Github Actions workflows)
    ├── app                     # FastAPI app files for the API endpoints
        ├── model               # App engine
        └── main.py             # Definition HTTP methods
    ├── config                  # Configuration of NGINX in docker container
    ├── docs                    # Sphinx documentation files (workflow builds html)
    └── test                    # Tests for app components (workflow runs all tests)

## Deployment
To deploy your app locally, follow the instructions below. For distribution purposes, it is convenient to link this GitHub repository to a DockerHub repository where you can store an image of your app that others can access directly. Follow [these instructions](https://docs.docker.com/docker-hub/builds/) to setup automated image building on DockerHub, based on changes to your GitHub repository, e.g. pushes to the main branch. 

### Locally
In order to run the docker container locally on non-Linux machines one needs to install [Docker Desktop](https://www.docker.com/products/docker-desktop) available for Mac and Windows.  

To spin up a container based on the image in your DockerHub repository, open a command prompt or terminal window and use the following command: 

```bash
docker run -d -p 5000:8080 YourDockerHubAccountName/YourDockerHubRepository:latest
```

In order to spin up a locally built version, navigate to the directory containing "docker-compose.yml" and run:

```bash
docker compose up --build
```

The API swagger documentation should now be available at [http://localhost:5000/docs/](http://localhost:5000/docs/).

## Documentation
The implementation of the API with Python package FastAPI ensures that Swagger UI documentation is readily available without additional steps. Please note that Swagger UI documentation assumes specific comment notation to extract the necessary information.  
Additionally, a GitHub workflow is setup such that a push to the master branch will rebuild Sphinx documentation from the files in the docs folder. The resulting html pages are located in the "gh-pages" branch. To host the Sphinx documentation from GitHub, go to Settings/GitHub Pages and select the "gh-pages" branch as Source. 

> :warning: Making your repository public will make it and its commit history available on the world wide web!

## Testing
The [pytest](https://docs.pytest.org/en/stable/) testing framework is used. Testing is performed automatically for pushes to the master branch based on tests located in the "tests" directory. Details on failed tests can be inspected further in the log files from the "Actions" menu. 
