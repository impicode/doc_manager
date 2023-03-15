
doc_manager
===========
.. image:: https://img.shields.io/badge/license-MIT-lightgrey
    :alt: License MIT
    :target: https://en.wikipedia.org/wiki/MIT_License

.. image:: https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue
    :alt: PyPI - Python Version
    :target: https://www.python.org/

.. image:: https://img.shields.io/badge/django%20versions-3.2%20%7C%204.0%20%7C%204.1-blue
    :alt: PyPI - Django Version
    :target: https://www.djangoproject.com/

**doc_manager** is a django library for publishing documents in pdf and html format like privacy policy or term of use. It allows you to easily publish new versions of documents while preserving historical documents.


Installation
------------

You can install module from pypi with pip: ::

    pip install doc-manager

or install it directly from the repository with pip: ::

    pip install git+ssh://git@github.com/impicode/doc_manager.git

for a specific branch: ::

    pip install git+ssh://git@github.com/impicode/doc_manager.git@branchname


Requirements
------------
- django>=3.2.17


Setup
-----

Add doc-manager to INSTALLED_APPS in settings.py file: ::

    INSTALLED_APPS = [
        ...
        'doc_manager',
        ...
    ]

Define the model in  ``our_app/models.py``: ::

    from doc_manager.models import DocumentModel

    class OurModel(DocumentModel):
        pass

Register the model in django admin, where the documents are published.
``our_app/admin.py`` changes: ::

    from doc_manager.admin import DocumentAdmin
    from .models import OurModel

    @admin.register(OurModel)
    class OurAdmin(DocumentAdmin):
        model = OurModel

Create a view responsible for displaying the pdf or html document and assign a specific url to it.

``our_app/views.py`` changes: ::

    from doc_manager.views import DocumentView
    from .models import OurModel


    class OurView(DocumentView):
        model = OurModel

Adding path to ``urls.py``: ::

    from our_app.views import OurView

    urlpatterns = [
        ...
        path('see_document/', OurView.as_view(), name = 'see_document'),
    ]

To add a link to the view of a published document, just: ::

    <a  href="{% url 'see_document' %}" target="_blank">See document</a>


Don't forget to migrate after adding a new model: ::

    python manage.py makemigrations
    python manage.py migrate


Usage
-----

- log in to the admin page
- head to app_name section
- add document
- publish document

Published document is now visible at the URL you previously specified in urls.py


Translations
------------

We provide translations only to Polish. If you need any other language run in doc_manager directory: ::

    django-admin makemessages -l <language code>

then in created file /locale/<language code>/LC_MESSAGES/django.po enter your translations and run: ::

    django-admin compilemessages

Now you have doc-manager app with your custom transltions ready to use in your project.


Example
-------

In main directory run: ::

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Then:

- Log in to the admin page (http://127.0.0.1:8000/admin/)
- Add document in OUR_APP/Our models
- Publish added document
- Go to http://127.0.0.1:8000/see_document/ to see added document


pre-commit Installation
-----------------------

In case of developing doc_manager itself please install pre-commit before your first commit. You can do it with the following commands: ::

    pip install pre-commit

Then in main directory: ::

    pre-commit install


Testing
-------

To run tests in main directory run: ::

    python runtests.py

You can also run tests with tox. In main directory run: ::

    tox

That command will run tests discribed above, pre-commit style checks against all files and build a test package with poetry.
