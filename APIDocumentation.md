# Base URL : http://127.0.0.1:5000

Login
POST /api/auth/login
Body (JSON)
{
  "email": "james@mail.com",
  "password": "123456"
}

Response
{
  "message": "Login successful",
  "access_token": "JWT_TOKEN",
  "user_id": 1
}


Create User
POST /api/users
Body
{
  "firstName":"John",
  "lastName":"Doe",
  "email":"john@mail.com",
  "password":"123456",
  "age":25,
  "city":"Chennai",
  "state":"TN",
  "country":"India",
  "zip":"600001",
  "company":"ABC",
  "web":"abc.com"
}

Response
{
  "msg": "User created"
}


Get All Users
GET /api/users

Some other ways of calling this route
GET /api/users?page=1&limit=5
GET /api/users?search=Emma
GET /api/users?sort=-age


# The below routes require token to be passed
Header required:
Authorization: Bearer TOKEN

Get User By ID
GET /api/users/id

Example:

GET /api/users/id
[Using token id can be retrieved]


Update User
PUT /api/users/update

Body
{
  "age":40,
  "city":"Bangalore"
}

Update User
PATCH /api/users/partial_update
Body
{
  "city":"Hyderabad"
}


# This uses id as param inside url for delete
Delete User
DELETE /api/users/{id}

Example:
DELETE /api/users/5

 # These give summary . No need of token etc
GET /api/users/summary
Response
{
  "average_age": 27.5,
  "users_by_city": {
    "Chennai": 2,
    "London": 1
  }
}