# Django Monolith Example
A django monolith example project for Amdaris Training monolith to microservices workflow

## Stack

- Python 3.12
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

1. Create a .env file based on the example

```commandline
cp .env.example .env
```
2. Generate a django secret hash
```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
3. Use this hash to set the value for **SECRET_KEY**
4. Generate a base 64 hash for signing the JWT token
```commandline
openssl rand -base64 64
```
5. Use that hash to set the value for **JWT_SIGNING_KEY**
6. Install dependencies
```commandline
make install
```
7. Create the db container
```commandline
make up
```
8. After db is healthy run the migrations
```commandline
make migrate
```
9. Now run the app
```commandline
make run_uvicorn
```

## Postman

Please use the provided postman collection to use the API.

Keep in mind the usual workflow should be like this:
1. Create a new user with POST register endpoint, if this is your first user and you want to give it permissions, use a DB client to set is_staff=true for it
2. Login the user with POST login endpoint, this will give you a token. You may use jwt.io to check the permissions included in the token based on your DB user.
3. With an admin (staff) account you may do PUT request to update your own user and add new permissions.
4. With the added permissions generate a new token by logging in again
5. Use the new token to do allowed operations on the pets api

## How to develop

1. Create feat/xyz branch from main
2. Create a PR
3. Make sure you always run both before commit
```commandline
make format_fix
make lint_fix
```
