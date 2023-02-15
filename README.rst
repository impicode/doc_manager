
doc_manager
===========


**doc_manager** is a django library for publishing documents in pdf format like privacy policy or term of use. It allows you to easily publish new versions of documents while preserving historical documents.


Installation
------------


To install module with pip: ::

    pip install git+ssh://git@github.com/impicode/doc_manager.git

for a specific branch: ::

    pip install git+ssh://git@github.com/impicode/doc_manager.git@branchname


Requirements
------------
- django==3.2.17


Setup
-----

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

Create a view responsible for displaying the pdf document and assign a specific url to it.

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
-------

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
- Go to http://127.0.0.1:8000/see_document/ to see added document.


pre-commit Installation
-----------------------

In case of developing doc_manager itself please install pre-commit before your first commit. You can do it with following commands: ::

    pip install pre-commit

Then in main directory: ::

    pre-commit install
