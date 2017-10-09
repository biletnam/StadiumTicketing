[![Build Status](https://travis-ci.org/gr1d99/StadiumTicketing.svg?branch=user-interface)](https://travis-ci.org/gr1d99/StadiumTicketing)

# StadiumTicketing
Is a Django powered web application that allows users to create and login to theire accounts.
Registered users can reserve and book tickets online.

## Demo
[http://tckt.herokuapp.com/](http://tckt.herokuapp.com/)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
See deployment for notes on how to deploy the project on a live system.

### Prerequisites
- Python3 [Installation](https://www.python.org/downloads/)
- Git [Installation](https://git-scm.com/downloads)

### Installation
1. clone the project 
   ```bash
    $ git clone https://github.com/gr1d99/StadiumTicketing.git
   ```
 2. Navigate to the root of the project
    ```bash
     cd Ticket
    ```
 3. Create a virtual enviroment.
    ```bash
     $ virtualenv --python=python3 env
    ```
    
    activate virtual enviroment
    
    ```bash
     $ env\Scripts\activate
    ```
    
 4. Intall dependencies.
    ```bash
     $ pip install -r requirements.txt
    ```
 5. In your browser type [localhost:8000](127.0.0.1:8000)
 