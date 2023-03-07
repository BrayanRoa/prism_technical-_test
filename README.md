# Management and control system

As a support for its employees, Prisma has considered developing a management and control system for expenses so they can control their monthly budget. For which it is requested to develop the Back-end layer services using the necessary technologies (you can use the technology that better drive, but preferably Python 🐍).

## Steps needed to run the project

1. Clone the repository
2. create your virtual environment 
  
  ```
  virtualenv venv
  ```
3. install the necessary libraries that are in the archive ```requirements.txt```

  ```
  pip install -r requirements.txt
  ```

4. Environment Variables 🚧

copy the variables that are in the ```.env.example``` file and create a file called ```.env``` where you should place these variables and fill them with the corresponding values

5. enter the following commands

```
export FLASK_APP=entrypoint
```
```
export FLASK_DEBUG=1
```
```
flask run
```

6. You can access the documentation in the following links:

```
http:localhost:5000/apidocs
```
```
https://web-production-7cec.up.railway.app/apidocs/
```

## Architecture

in this project, the rest architecture was used to design the api that allows the different parts of the system to communicate with each other. for this, a set of identifiable resources was defined, each with its own unique url, and it was defined how these resources could be manipulated through different http methods (get, post, put, delete).

this architecture was chosen because it allows high scalability and flexibility, since new resources and functionalities can be added without affecting the general structure of the system.

![Architecture](https://github.com/BrayanRoa/prism_technical-_test/blob/main/architecture.jpg?raw=true "Architecture")

This project is divided into two modules, users and authentication, the auth module is in charge of validating the input information of each of the users that are registered in the system.

The user module is in charge of the administration of each and every one of the bills that each user has, this administration is possible thanks to the implementation of the http verbs (get, post, put, delete)
# Stack

<p align="center">
  <a target="blank"><img src="https://process.filestackapi.com/cache=expiry:max/resize=width:700/Fyt43eEpRUehYxfjwa7o" width="300" alt="python-flask-postgresql-docker" /></a>
</p>