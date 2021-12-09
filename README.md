# Infrastructure-containerized-Application
Application deployed on AWS ECS Infrastructure

## STACK
* language: Python3
* Framework: flask
* Infrastructure: Docker
* Cloud Deployment: AWS and Terraform

## SOLUTION APPROACH
### Code
Flask framework is used to build this API. Tests are also done with the native python test suite. 

### Infrastructure
Docker is used to maintain infrastructure deployment and ensure deploying to an isolated environment 

## TESTING
* In order to run the tests for the application locally run ```python tests.py```. This is also included in the docker build step to ensure only code that passed tests is built.


### Deploying with Docker
* This solution is deployed using Docker. 

- Build docker image; Run the below command within the folder that contains the DockerFile

```
cd Application

```

```
docker build --tag container-app .
```

- Running the docker container

```
docker run -d --name factorial_app -p 5000:5000 container-app
```

### Running locally
To run the code locally (out of docker)
* Test with ```python tests.py```
* Start API with ```FLASK_APP=api.py flask run```


### ACCESS API ENDPOINTS (LOCALLY)
To access the API, you can use PostMan or any other HTTP Client of your choice

* To get all users ```GET``` to http://localhost:5000/factorial?value=5

```
{"function":"factorial","input":"5","output":120}

```

* For health checks ```GET``` to http://localhost:5000/



### Deploy to AWS Using Terraform
To deploy this solution to the cloud, two main technologies are required -- Cloud platform(AWS), Terraform

- Terraform -- Terraform would be used to instantiate and manage the infrastructure the application would run on, this means, we get the ability to manage the state and the lifecycle of the infrastructure using terraform workflow

- Cloud Platform -- Any cloud provider is fine for deployment, For AWS, I leverage the following service

```
- AWS ECS -- Fargate
- Docker -- For hosting the container
- IAM -- Access and Security
- LB -- Loadbalancing
- Security Groups
- AWS VPCs
- AWS Cloudwatch

```

### Terraform Structure
The IaC code is modularized, meaning, it is built into reusable modules called child module, the child module is located at:

```
cd infrastructure
```

Also built with the child module, is a deployable module called the root module. The root module installs and uses resources defined in the child module for deployment. The root module and instructions on deployments can be found here:

```
cd infrastructure/application_deployment
```
- A README with instructions on how to deploy the infrastructure is placed at in the folder.

==> The docker container with the code base has been pre-built and deployed to a public repository for easy pull and deployment.


### Infrastructural Diagram and Reference

![ECS infra](img/infrastructure/infra_diag.png)
