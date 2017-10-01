# StadiumTicketing
Is a Django powered web application that allows users to create and login to theire accounts.
Registered users can reserve and book tickets online.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
See deployment for notes on how to deploy the project on a live system.

## Prerequisites
- Python3 [Installation](https://www.python.org/downloads/)
- Git [Installation](https://git-scm.com/downloads)

## Installation
1. clone the project 
   ```bash
    $ git clone https://github.com/gr1d99/StadiumTicketing.git
   ```
 
 2. Create a virtual enviroment.
    ```bash
     $ virtualenv --python=python3 env
    ```
    
    activate virtual enviroment
    
    ```bash
     $ source env/bin/activate
    ```
    
 3. Intall dependencies.
    ```bash
     $ pip install -r requirements.txt
    ```
   
 4. create `secret.ini` file in the root of the project and copy the contents below to the file.
   
    ```ini
    [DEFAULT]
    SECRET_KEY: <secret key goes here>
    ```
 5. Run the server.
    ```bash
     python manage.py runserver
    ```
 
 6. In your browser type [localhost:8000](127.0.0.1:8000)
 