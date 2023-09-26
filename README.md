# MountainPass
Learning project, REST API on Django, backend of imaginary android/OS app for sending information about mountain passes

### Installation
Use any IDE (integrated development environment) that supports Python, PyCharm - recommended.\
Install and run PostgreSQL or other database of your choice. Find file mpass/mpass/config.py then fill the variables up with your DB information.
> FSTR_DB_HOST = "127.0.0.1"\
> FSTR_DB_PORT = "5432"\
> FSTR_DB_LOGIN = "postgres"\
> FSTR_DB_PASS = "jenga"

Now we want to create tables in the database. In your IDE go to mpass folder and run commands:
> python manage.py makemigrations\
> python manage.py migrate

That's it.

### How To Use
You want to fill up your tables. In browser, go to **http://127.0.0.1:8000/admin/**, log in as superuser:
> login: biorival\
> password: jenga\

Fill up Activity types with what fits you, examples: "on foot", "bike", "climbing"\
Fill up Areas with a name of each region you want to keep track off, examples: "Himalayas", "Alps", "Umbrail Pass"

Whoever sends data from their imaginary android/OS app, will send it to **http://127.0.0.1:8000/submitData/**, \
this will usually influence table PerevalAdded\
It consists of:
> **beauty_title** - prefix to a title, if necessary\
> **title** - title of a mountain pass or other area\
> **other_titles** - alternative title or some descriptors, if necessary, such as (north-west) or (far away)\
> **connect** - a mystery, something you shouldn't touch\
> **spring** - difficulty of moving through the area during respective seasons, possible choices - 00 (unknown), 1A, 1B, 2A, 2B, 3A, 3B\
> **summer** - same as above\
> **autumn** - same as above\
> **winter** - same as above\
> **status** - possible choices: new, pending, accepted, rejected. When recieved from a user, by default it's - new. Later you can read the information and change status to what you see fit. After this, any attempts to edit it through API means is locked.\
> **latitude** - decimal number representing north–south position of a point on the surface of the Earth\
> **longitude** - decimal number representing west-east position of a point on the surface of the Earth\
> **height** - integer number representing the shortest distance between subject's location and the sea level\
> **email** - email of the user, must be unique, duplicates not allowed\
> **phone** - phone number of a user\
> **surname** - surname of a user\
> **firstname** - firstname of a user\
> **patronymic** - patronymic of a user, if necessary\
> **photo** - list of photos of an area with: **title** - name of an image, **photo** - the data itself

Methods:
> **POST** - supplied with valid json information, will create a new instance with a status new. If the email provided was not registered in database, will create a new user automatically\
> **GET** - returns a full list of all instances submitted\
> **GET (with a parameter user__email)** - will return all instances sent by a user with specified email,\
> example - /submitData/?user__email=NormanJaydenFBI@gmail.com\
> **GET (with primary key)** - will return one instance based on the specified ID, example - /submitData/2\
> **PATCH** - edit information if status is *new*, otherwise you'll be denied. Also you can't change information about the user if provided email is already in the database

### JSON Example
```JSON
{
    "beauty_title": "pass",
    "title": "New Big Test",
    "other_titles": "hmmm",
    "connect": "",
    "spring": "1A",
    "summer": "1A",
    "autumn": "1B",
    "winter": "00",
    "coords": {
        "latitude": 13412.314,
        "longitude": 4134.24323,
        "height": 12432
    },
    "status": "1",
    "author": {
        "email": "summer@gmail.com",
        "phone": "+123412",
        "surname": "Sanchez",
        "firstname": "Morty",
        "patronymic": "Jerryvich"
    },
    "photos": [{"photo":"<img1>", "name":"Eagles Eye"}, {"photo":"<img2>", "name":"Bear Claw"}]
}
```

