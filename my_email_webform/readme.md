# Email Webform App

The purpose of this app is to insert name and emails of users through a simple web form interface. the app is built using python, flask and containerized using docker.

## Features

- insert names and emails of users and store in a SQLite database.

## Requirements

- Python 3.9 or higher 
- Docker Desktop
- Flask
- Werkzeug

## Procedure

### 1: Navigate to the project directory

- cd my_email_webform

### 2: Open Docker Desktop

- Open Docker Desktop application

### 3: Create Docker Image (Run command in command prompt/terminal)

- docker build -t my_email_webform .

### 4: Running the Docker image by running the below command

- docker run -p 5000:5000 my_email_webform

#### Author - Likhith Gunjal - G23AI2092