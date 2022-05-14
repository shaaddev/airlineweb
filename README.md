# Airline Web

Airline Website Basic Project


## Set up

Install virtual environment

$ python3 -m venv virt

Create virtual environment

$ source virt/bin/activate

After creating virtual environment, it should look like this:

(virt) file_name $

## Install Django and other requirements

$ pip install django

$ pip install bcrypt

$ pip install argon2


## Build and run production

Make Migrations

$ python3 manage.py makemigrations 

$ python3 manage.py migrate


Start up Django

$ python3 manage.py runserver
