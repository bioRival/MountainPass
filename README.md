# MountainPass
Learning project, REST API on Django backend of imaginary android/OS app for sending information about mountain passes

### Installation
Use any IDE (integrated development environment) that supports Python, PyCharm - recommended.\
Install and run PostgreSQL or other database of your choice. Find file mpass/mpass/config.py then fill the variables up with your DB information.
> FSTR_DB_HOST = "127.0.0.1"\
> FSTR_DB_PORT = "5432"\
> FSTR_DB_LOGIN = "postgres"\
> FSTR_DB_PASS = "jenga"

Now we want to create tables in the database. In your IDE go to mpass folder and run commands:\
> python manage.py makemigrations\
> python manage.py migrate

That's it.

### How To Use
You want to fill up your tables. In browser, go to **http://127.0.0.1:8000/admin/**, log in as superuser:
> login: biorival\
> password: jenga
Fill up Activity types with what fits you, examples: "on foot", "bike", "climbing"\
Fill up Areas with a name of each region you want to keep track off, examples: "Himalayas", "Alps", "Umbrail Pass"

Whoever sends data from their imaginary android/OS app, will send it to **http://127.0.0.1:8000/submitData/**, this will usually influence table PerevalAdded\
It consists of:\
beauty_title - prefix to a title, if necessary\
title - title of a mountain pass or other area\
other_titles - alternative title or some descriptors, if necessary, such as (north-west) or (far away)\
connect - a mystery, something you shouldn't touch\
spring - difficulty of moving through the area during respective seasons, possible choices - 00 (unknown), 1A, 1B, 2A, 2B, 3A, 3B\
summer - same as above\
autumn - same as above\
winter - same as above\
status - possible choices: new, pending, accepted, rejected. When recieved from a user, by default it's - new. Later you can read the information and change status to what you see fit. After this, any attempts to edit it through API means is locked.
latitude - decimal number representing north–south position of a point on the surface of the Earth
longitude - decimal number representing west-east position of a point on the surface of the Earth
height - integer number representing the shortest distance between subject's location and the sea level


Here's a few options API can do:
submitData/ POST - if sent with valid information, will save 

