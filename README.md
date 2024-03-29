# API Project

## Description

A simple containerized Flask API and SQLite application to store users.

## Requirements

1. Python3 installed along with PIP
2. Docker installed

## How To Run

1. Clone repo to your destination.
2. Run build_and_test Bash script in your terminal

Docker will Build the two containers, one API and one SQLite. The script will also run a test hitting each of the endpoints. Lastly, the sript will tell user the API is live. You will be able to hit the API on ```http://localhost:8000/```

## Using and Testing the API

You can interact with the API by making curl commands.

### GET

Health Checker
```bash
curl http://localhost:8000/api/healthchecker
```

Get Users
```bash
curl http://localhost:8000/users
```

### POST

Create User

```bash
curl --header "Content-Type: application/json" \
--request POST --data '{"name":"USER", "username":"USERNAME", "email":"USER@mail.com"}' \ 
http://localhost:8000/user
```

### PUT

Update User

```bash
curl --header "Content-Type: application/json" \
--request PUT --data '{"id": 1, "name":"USER2", "username":"USERNAME2", "email":"USER@mail.com"}' \ 
http://localhost:8000/user
```

### DELETE

Delete User

```bash
curl --request DELETE http://localhost:8000/user/1
```

## Future Iterations

- Develop CD Pipeline with Github Actions
    - This could be accomplished with deploying to an K8s Cluster or on an EC2 running Docker.
- Build out the Database with more complex tables