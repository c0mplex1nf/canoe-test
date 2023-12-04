
# Canoe Fund Test Project Documentation

## Authors
- [@c0mplex1nf](https://github.com/c0mplex1nf)

## Overview

The Canoe Fund Test project is a sophisticated financial application designed to manage and track investment funds. This document outlines the key architectural decisions, design patterns, and technology choices made during the development of this application.

## Architectural Overview

### Domain-Driven Design (DDD)

We have adopted Domain-Driven Design (DDD) to align the software design closely with the project’s domain complexities. This approach helps in tackling complex business requirements effectively and facilitates communication with domain experts.

- **Entities and Value Objects**: Key domain entities are identified to represent the core business concepts.
- **Repositories**: Repositories are implemented for accessing domain entities.

### Event Sourcing

The Canoe Fund Test project utilizes Event Sourcing to persist the state of domain entities as a sequence of state-changing events. This approach allows us to:

- Ensure a reliable audit trail of operations.
- Facilitate event-driven architecture to react to state changes.

### Hexagonal Architecture (Ports and Adapters)

To achieve a high level of modularity and maintainability, the Hexagonal Architecture model is employed. This architecture allows us to:

- Decouple the application’s core logic from external concerns.
- Define clear interfaces (ports) for the application’s interaction with the outside world.
- Implement adapters for external communications such as UI, API, and external services.

## Technology Stack

### Database Selection

![ER Diagram](https://i.ibb.co/881vvWL/canoe-drawio-1.png)

#### SQL Database: SQLite (For Testing)

- **Purpose**: During the initial development and testing phases, SQLite is used for its simplicity and ease of integration.
- **Scope**: SQLite handles regular transactional data efficiently in a testing environment.

#### Recommendation for Production

- **NoSQL Database for Logs**: Considering the nature of Event Sourcing and the need for efficient log management, a NoSQL database is recommended for handling logs. NoSQL databases offer scalability and flexibility, making them ideal for storing and querying large volumes of log data.

- **Powerful SQL Database**: For handling complex queries and transactional data in production, a more powerful SQL database is recommended. This choice will cater to the need for robustness, consistency, and performance in handling financial transactions.



## API Reference

### (There is a postman file inside the project to test)

# Project: Canoe

## End-point: Create Company
### Method: POST
>```
>localhost:8000/company
>```
### Body (**raw**)

```json
{
    "name": "test1"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Create Manager
### Method: POST
>```
>localhost:8000/manager
>```
### Body (**raw**)

```json
{
    "name": "test2"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Create Fund
### Method: POST
>```
>localhost:8000/fund
>```
### Body (**raw**)

```json
{
    "name": "test_fund",
    "start_year": "2023",
    "alias": "test_fund_alias",
    "nationality": "USA",
    "manager": "6f60e7ab-6f37-4323-9309-15ccdbf55803",
    "companies": ["b1049dec-1694-4ffd-b2cf-ae3a6ffa9278"]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: List Funds
### Method: GET
>```
>localhost:8000/fund?skip=0&take=1&manager=d3768c0a-95aa-4acb-88e0-101b01b96fbc&start_year=2023&name=test
>```
### Query Params

|Param|value|
|---|---|
|skip|0|
|take|1|
|manager|d3768c0a-95aa-4acb-88e0-101b01b96fbc|
|start_year|2023|
|name|test|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update Fund
### Method: PUT
>```
>localhost:8000/fund/311166f8-225b-4670-b0dc-0675beac9a46
>```
### Body (**raw**)

```json
{
    "name": "test2",
    "start_year": "2023",
    "alias": "test_fund_alias_2",
    "nationality": "USA",
    "manager": "d3768c0a-95aa-4acb-88e0-101b01b96fbc",
    "companies": ["86c696ad-7b29-4c52-8a21-1493f0fd4ecd", "4ced687c-f1d7-41e6-b97d-0bfb57e98ea1"]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete Fund
### Method: DELETE
>```
>localhost:8000/fund/205f9459-e58e-45f1-bf07-1406f0cf1e70
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: List Duplicate Funds
### Method: GET
>```
>localhost:8000/fund/duplicate?skip=0&take=10
>```
### Query Params

|Param|value|
|---|---|
|skip|0|
|take|10|

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: List Companies
### Method: GET
>```
>localhost:8000/company
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: List Managers
### Method: GET
>```
>localhost:8000/manager
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# Deployment Process Using Docker-Compose

This part describes the steps for deploying the application using Docker and `docker-compose`. The process is straightforward and primarily involves building the Docker images and then starting the containers.

## Prerequisites

Before starting, ensure you have the following installed:
- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

Ensure that you have the `docker-compose.yml` file at the root of your project, defining the services, networks, and volumes needed for your application.

## Deployment Steps

### 1. Clone the Repository (If Necessary)

If you haven't already, clone your project repository to your local machine or server.

```bash
git clone [your-repository-url]
cd [your-project-directory]
```

### 2. Build the Docker Images

Run the following command to build the Docker images as defined in your docker-compose.yml file. The --no-cache option ensures that the images are built from scratch, providing a clean, up-to-date build.

```bash
docker-compose build --no-cache
```

### 3. Start the Containers

Once the build process is complete, start the containers with the following command:


```bash

docker-compose up -d
```

This Should be all

## Roadmap

- There are some pattern that are missign because of time

- Implement Saga pattern

- Make integration test with the use of the queues

- Make agreggators for the entities

- Re use some parts of the code

## Tech Stack

This section outlines the technology stack used in our project, providing details on the server environment, infrastructure components, and key libraries.

### Server

- **Python**: A high-level, interpreted programming language known for its readability and versatility. Used as the primary programming language for backend development.
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

### Infrastructure

- **Docker**: An open platform for developing, shipping, and running applications in isolated environments called containers.
- **Docker-Compose**: A tool for defining and running multi-container Docker applications. It uses YAML files to configure application services and simplifies the deployment process.
- **RabbitMQ**: An open-source message broker software that accepts and forwards messages. It's lightweight and easy to deploy on-premises and in the cloud.

### Libraries

- **pydantic**: A data validation and settings management library using Python type annotations.
- **uvicorn**: An ASGI server for Python, built on uvloop and httptools, used to run FastAPI applications.
- **asyncio**: A Python library for writing concurrent code using the async/await syntax.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **alembic**: A lightweight database migration tool for usage with SQLAlchemy.
- **python-dotenv**: A Python library for reading key-value pairs from a `.env` file and setting them as environment variables.
- **requests**: An elegant and simple HTTP library for Python, built for human beings.
- **pika**: A pure-Python implementation of the AMQP 0-9-1 protocol used for RabbitMQ.
- **aio_pika**: An asynchronous library based on `pika` for working with RabbitMQ, utilizing `asyncio`.


# Application Scalability Overview

## Handling Increasing Data Size

### Database Performance and Scaling

- **SQLAlchemy & Alembic**: 
  - Our use of SQLAlchemy as an ORM helps manage complex queries and relationships efficiently. As our dataset grows, we can optimize queries and adapt our database schema as needed.
  - Alembic assists in smooth database migrations, which are crucial when evolving our database structures in response to growing data.
  - As the data grows, we might consider implementing database sharding or partitioning to distribute the data load.

- **Infrastructure Scaling**:
  - We leverage Docker and Docker-Compose for scaling services. As data load increases, these tools allow us to replicate and scale our application's services effectively.

### Efficient Message Processing

- **RabbitMQ**: 
  - Our application uses RabbitMQ for handling a large volume of messages, ensuring message processing and task distribution remain efficient even as data grows.

## Handling Increasing Number of Concurrent Users

### FastAPI Performance

- As a high-performance framework, FastAPI allows our application to handle more requests per second per worker. This is particularly beneficial as the number of concurrent users increases.

### Asynchronous Programming

- **Asyncio & aio_pika**: 
  - We use asyncio for asynchronous programming, improving our application's ability to handle large numbers of concurrent connections without blocking on I/O operations.
  - aio_pika integrates RabbitMQ with asyncio for efficient message queue handling, even under high concurrent loads.

### Optimized Infrastructure

- **Docker**:
  - Docker's containerization approach ensures that each component of our application can be independently scaled. As user load increases, we can scale specific components, such as the web server or database, according to the demand.


[MIT](https://choosealicense.com/licenses/mit/)

