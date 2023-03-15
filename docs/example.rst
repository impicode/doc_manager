#######
Example
#######

===========
Run example
===========

In main directory run: ::

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Then:

- Log in to the admin page (http://127.0.0.1:8000/admin/)
- Add document in OUR_APP/Our models
- Publish added document
- Go to http://127.0.0.1:8000/see_document/ to see added document.
