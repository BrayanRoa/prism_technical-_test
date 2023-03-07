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


## some technologies used for the implementation of the API

* Flask: Lightweight Python web framework for building web applications. It enables you to quickly build scalable and flexible web applications with clean, maintainable code.

* SQLAlchemy: A Python object-relational mapping library for interacting with relational databases. It provides an easy way to create and manage database schemas and allows portability between different databases.

* Marshmallow: A Python serialization and deserialization library for converting complex Python objects to JSON, XML, and other data formats. Allows data validation and schema creation to ensure data consistency.

* Flask-Swagger: A library that adds support for API documentation using the OpenAPI (formerly known as Swagger) specification. It provides an easy way to generate documentation for APIs and API clients.

* Railway: Plataforma en la nube para alojar y administrar aplicaciones web. Permite a los desarrolladores alojar aplicaciones web de forma rápida y sencilla, con integraciones nativas para bases de datos, caché, correo electrónico y otras funcionalidades.

## Tthe users module was divided into:

+ Controller: It is the software component that handles the presentation logic and user interaction. In other words, the controller is responsible for processing the user's requests, collecting the necessary data and sending a response to the user's web browser.

* Service: On the other hand, a service is a software component that handles the business logic of the application. Services often provide reusable functionality that can be used by different parts of the application.

* Entity: In other words, an entity is an abstraction of a real world object or concept that is important to the business or operation of the application. For example, in our application, the user entity represents the data of a client, such as their username, email and password.

* Schema: Within Marshmallow, a "schema" refers to a class that defines the structure of an object to be serialized or deserialized. A Marshmallow schema is used to specify the fields to include in a serialized object and to validate the data that is used to create an object.

* Models: DTOs are a way to encapsulate data and reduce coupling between different parts of an application. Instead of passing domain objects or entire entities between application layers, DTOs are used to transfer only the necessary data.

# Stack

<p align="center">
  <a target="blank"><img src="https://process.filestackapi.com/cache=expiry:max/resize=width:700/Fyt43eEpRUehYxfjwa7o" width="300" alt="python-flask-postgresql-docker" /></a>
</p>