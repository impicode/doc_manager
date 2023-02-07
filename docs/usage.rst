##########
How to use
##########


==========
Simple use
==========

Setup
=====

First, you need to add an application that will be responsible for the documents (here ``our_app``).

The next step is to define the model in  ``our_app/models.py``:::

    from doc_manager.models import DocumentModel

    class OurModel(DocumentModel):
        pass

Each model is responsible for one document type. For example, if we want to have both regulations and a privacy policy on the website, we will need two models.

The next step is to register the model in django admin, where the documents are published.
``our_app/admin.py`` changes:::

    from doc_manager.admin import DocumentAdmin
    from .models import OurModel

    @admin.register(OurModel)
    class OurAdmin(DocumentAdmin):
        model = OurModel

*DocumentAdmin* class gives us access to publish functionality.

The next step is to create a view that will be responsible for displaying the pdf document and assign a specific url to it.

``our_app/views.py`` changes:::

    from doc_manager.views import DocumentView
    from .models import OurModel


    class OurView(DocumentView):
        model = OurModel

Adding path to ``urls.py``:::

    from our_app.views import OurView

    urlpatterns = [
        ...
        path('see_document/', OurView.as_view(), name = 'see_document'),
    ]

To add a link to the view of a published document, just:::

    <a  href="{% url 'see_document' %}" target="_blank">See document</a>


Don't forget to migrate after adding a new model::

    python manage.py makemigrations
    python manage.py migrate

Usage
=====

- log in to the admin page
- head to app_name section
- add document
- publish document

Published document is now visible at the URL you previously specified in urls.py
