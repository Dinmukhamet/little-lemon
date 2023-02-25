
# Little Lemon

This is the final assignment for the Meta course "Back-End Developer Capstone" at coursera.



## Installation 

### Introduction

This project requires you to have poetry installed on your system. Poetry is a tool for dependency management and packaging in Python.

### Virtual Environment

After installing poetry, you can create a virtual environment in which to run the project. You can create a virtual environment any way you like, but if you prefer to use the venv module, you can create a virtual environment by running the following command:

```bash
python -m venv venv
```

If you don't want to create a virtual environment yourself, poetry can do it for you by running:

```bash
poetry install
```

To activate the virtual environment, run:

```bash
source venv/bin/activate
```

Note: If you are using Windows, the command to activate the virtual environment may be different.

### Dependencies

Once you have activated the virtual environment, you can install the project's dependencies by running:

```bash
poetry install
```

### Running the Development Server

To run the development server, use the following command:

```bash
poetry run python manage.py runserver
```

### MySQL Database

To use this project, you will need to install and configure MySQL database. There are several ways to get a working MySQL database. The easiest way would be to use a Docker image.

### Environment Variables

The project depends on several environment variables. You can set these variables by creating a .env file in the root directory of the project. Here is an example .env file:

```makefile
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=mysql://username:password@host:port/name
```

Make sure to replace the values of the environment variables with your own values.
## Deployment

### Docker Configuration

This project includes a Docker configuration that allows you to easily deploy the project as a Docker container.
Running with Docker

To run the project using Docker, first make sure you have Docker installed on your system. Then, navigate to the project directory and run the following command:

```bash
docker-compose up -d --no-deps --build
```

This command will build or pull the necessary images and start the containers for both the API and the database.

### Docker Compose Configuration

The Docker Compose configuration for this project is defined in the docker-compose.yml file. You can modify this file to adjust the configuration of the containers and their dependencies.

Note that you may need to modify the environment variables in the docker-compose.yml file to match your specific deployment requirements.
## Running Tests
### Introduction

This project includes a suite of tests that you can run to ensure that everything is working correctly. The tests are written using the pytest library.

### Installing Test Dependencies

Before you can run the tests, you will need to make sure that the test dependencies are installed. If you are using poetry, you can install the test dependencies by running:

```bash
poetry install --with test
```

### Running the Tests

To run the tests, use the following command:

```bash
poetry run pytest
```

This will run all the tests in the project and report the results. If any tests fail, you will see an error message with details about the failure.

Note that you can also run specific tests by specifying the name of the test file or function to run. For example, to run the tests in the test_foo.py file, you would run:

```bash
poetry run pytest test_foo.py
```
## Authors

- [@dinmukhamet](https://www.github.com/dinmukhamet)


## License

[MIT](https://choosealicense.com/licenses/mit/)


## 🚀 About Me
Hello, my name is Dinmukhamet. I am currently pursuing a master's degree at Satbayev University. I am working on this project as a part of the "High Load Distributed Computing" course.

