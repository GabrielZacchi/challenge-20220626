**This is a challenge by Coodesh**

# Fitness Foods LC - Open Food Facts REST API

## Introduction

This project is a REST API that utilizes data from the Open Food Facts database, an open database containing nutritional information of various food products. The project's objective is to support the nutritionist team at Fitness Foods LC in quickly comparing the nutritional information of foods in the Open Food Facts database.

This challenge was provided by Coodesh as part of the Fullstack Challenge 20220626.

## Technologies Used

- Python Django
- Poetry (package management)
- MongoDB (Atlas for database hosting)
- REST Framework
- Schedule (for task scheduling)
- DRF-YASG (for OpenAPI API documentation)

## Installation and Usage

To run the project, follow these steps:

1. Clone the GitHub repository:

```bash
git clone https://github.com/GabrielZacchi/challenge-20220626.git
cd challenge-20220626
```

2. Set up the virtual environment and install dependencies:

```bash
poetry install
```

3. Create a `.env` file in the project's root directory with the following content:

```dotenv
# Django Settings
SECRET_KEY='django-insecure-yyir_16fbk5buvpmc8wr3e$zcp@iy)5sgmp^lmrgk!j3x*5=pg'

# Database Settings
DB_USERNAME='dbmanager'
DB_PASSWORD='mvlXCF5f9bMRqqRg'
DB_NAME='fitness_foods_lc'

# Scheduler Settings
PRODUCTS_LIMIT=10
RUN_TIME='08:00'

# Email Settings
ENABLE_EMAIL_LOG='False'
SENDER_EMAIL=''
RECEIVER_EMAIL=''
SMTP_SERVER=''
SMTP_PORT=''
SENDER_EMAIL_USERNAME=''
SENDER_EMAIL_PASSWORD=''
```

4. Create a MongoDB database using Atlas or any other SQL database, if preferred.

5. Set the correct database connection settings in the `.env` file (DB_USERNAME, DB_PASSWORD, DB_NAME) to connect to your database.

6. Optionally, configure the email settings in the `.env` file (ENABLE_EMAIL_LOG, SENDER_EMAIL, RECEIVER_EMAIL, SMTP_SERVER, SMTP_PORT, SENDER_EMAIL_USERNAME, SENDER_EMAIL_PASSWORD) for email alerts in case of synchronization failures.

7. Run the development server:

```bash
poetry run python core/manage.py runserver
```

8. Run the scheduler for periodic synchronization:

```bash
poetry run python core/scheduler.py
```

## API Endpoints

- `GET /`: Returns Status 200 and the message "Fullstack Challenge 20201026"

- `GET /products/:code`: Retrieves information of a specific product based on its code.

- `GET /products`: Lists all products in the database. The response is paginated to avoid request overload.

## Extras

- The project uses Docker for easy deployment by the DevOps team (Dockerization is optional).

- An alert system is implemented to notify the team in case of synchronization failures (EMAIL settings in the `.env` file).

- The API documentation is described using the OpenAPI 3.0 concept, accessible through the Swagger UI.

- Unit tests are written for API endpoints to ensure their functionality.

To run unit tests, execute the following command:

```bash
poetry run python core/manage.py test
```

Ensure that the `.env` file is correctly configured with the database and email information to ensure the project's proper functioning.