from django.shortcuts import render
from doc_manager.views import DocumentView

from .models import OurModel


class OurView(DocumentView):
    model = OurModel
