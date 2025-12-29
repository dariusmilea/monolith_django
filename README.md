# Django Monolith Example
A django monolith example project for Amdaris Training monolith to microservices workflow

## Stack
- Django
- Django Rest Framework
- PostgresSQL
- UV
- Ruff
- Docker

## Architecture

The monolith has 2 apps:
1. The pet api, which is a simple CRUD for pet entities
2. Authenticator API which allows users to create tokens to access endpoints from the pet api

## Key features

The pet API is a simple REST api which allows the user to
- Create pet records
- Read pet records
- Update pet records
- Delete pet records

Each endpoint is accessible to the user if the JWT token used to make these requests has the role to do any of the actions.
For this we use the second app which allows users to authenticate and get a JWT token which will allow them to operate the pet API.

## How to deploy locally

```commandline
cp .env.example .env
make up
make install
make migrate
make run-uvicorn
```
