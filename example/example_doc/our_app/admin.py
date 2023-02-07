from django.contrib import admin
from doc_manager.admin import DocumentAdmin

from .models import OurModel


@admin.register(OurModel)
class OurAdmin(DocumentAdmin):
    model = OurModel
