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

superuser: biorival
password: jenga
