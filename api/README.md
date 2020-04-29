#### Special Park REST API - Documentation

---

# Overview

1. [Run server](#run_server)
2. [Registration](#register)
3. [Authentication](#auth)
4. [Add a car](#add_car)
5. [Retrieve all cars](#get_cars)
6. [Delete a car](#delete_car)
7. [Update a car](#update_car)
8. [Start a parking session](#start_parking)
9. [Stop a parking session](#stop_parking)

## Run server <a name="run_server"></a>

How to start up the REST API on localhost to interact with the database. [Postman](https://www.postman.com/) is supported for sending requests. Python 3 is required and the module [pipenv](https://github.com/pypa/pipenv). Don't forget to rename the .env.example to .env and fill out your database credentials. Because we're using Django, you may have to run a [migration](https://docs.djangoproject.com/en/3.0/topics/migrations/). If you've completed these steps, you can run this command and the server will start up.

```
yarn api

>> Starting development server at http://127.0.0.1:8000/
```

## Registration <a name="register">

Register an consumer account.

##### URL
```
POST http://127.0.0.1:8000/users/registration/
```

##### BODY
```
{
    "username": "joker1234",
    "email": "joker1234@gmail.com",
    "password1": "vitamineD",
    "password2": "vitamineD"
}
```

###### RESPONSE
```
>> "key": "e399db4883c7018c5f52500f6c9221f4e75af5e5"
```

## Authentication <a name="auth">

Login and obtain a session key (token).

##### URL
```
POST http://127.0.0.1:8000/users/login/
```

##### BODY
```
{
    "username": "joker1234",
    "email": "joker1234@gmail.com",
    "password": "vitamineD"
}
```

###### RESPONSE
```
>> "key": "e399db4883c7018c5f52500f6c9221f4e75af5e5"
```

## Add a car <a name="add_car">

Add an license plate to your account using the token.

##### URL
```
POST http://127.0.0.1:8000/users/car/
```

##### BODY
```
{
    "license_plate_number":"46-nn-sr",
    "license_country_code": "NL"
}
```

##### HEADER
```
{
    "Authorization": "Token your_token"
}
```

###### RESPONSE
```
>> "message": "new car has been added!"
```

## Retrieve all cars <a name="get_cars">

Get all license plates attached to your account.

##### URL
```
GET http://127.0.0.1:8000/users/car/
```

##### HEADER
```
{
    "Authorization": "Token your_token"
}
```

###### RESPONSE
```
>> "cars": {...}
```

## Delete a car <a name="delete_car">

Delete a car from your account.

##### URL
```
DELETE http://127.0.0.1:8000/users/edit_car/your_license_plate
```

##### HEADER
```
{
    "Authorization": "Token your_token"
}
```

###### RESPONSE
```
>> "message": "car deleted"
```

## Update a car <a name="update_car">

Update an existing license plate.

##### URL
```
PUT http://127.0.0.1:8000/users/edit_car/your_license_plate
```

##### BODY
```
{
    "license_country_code": "NL",
    "license_plate_number": "19-JJ-00"
}
```

##### HEADER
```
{
    "Authorization": "Token your_token"
}
```

###### RESPONSE
```
>> "message": "Your car has been updated"
```

## Start a parking session <a name="start_parking">
##### URL
```
POST http://127.0.0.1:8000/garage/garage_hash/your_license_plate
```

##### BODY
```
{
    "service": "enter"
}
```

###### RESPONSE
```
>> "status": true
```

## Stop a parking session <a name="stop_parking">
##### URL
```
POST http://127.0.0.1:8000/garage/garage_hash/your_license_plate
```

##### BODY
```
{
    "service": "exit"
}
```

###### RESPONSE
```
>> "status": true
```