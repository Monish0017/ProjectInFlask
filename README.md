# Project Setup and Running

First create virtual Environmet . This is made using python 3.14 ( which is LTS Version)

commands to create those 
-> After cloning from github . Move to PROJECT - 1 Folder

Command : cd PROJECT - 1

-> Then create venv

Command : python3 -m venv flask_env 
[ For Folder Name you can use your own name also]

-> Install all the requirements which are all in the requirement.txt

Command : pip install -r requirements.txt

-> Run the below command to start the flask App.

Command : python3 app.py

[You can see in terminal it will be hosted in 5000 port or something]


# PostMan

Dowload postman extension in vs code then sign in with your google account

-> After that test apis whether they are running 
-> API Documentation is there in my repo also . you can check what are the params , body part , tokens to passed for each api's


# Libray Used

Flask	               Web framework
Flask-SQLAlchemy	   ORM (like Mongoose)
Flask-JWT-Extended	   Authentication (JWT)
Passlib	               Password hashing
bcrypt	               Hashing backend
SQLite	               Local database
SQLAlchemy	           Query builder / ORM core

# For post check , you can use user.json Mock datas

user.json
