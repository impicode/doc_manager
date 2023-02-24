from django.contrib import admin
from doc_manager.admin import DocumentAdmin
from tests.models import TestModel


@admin.register(TestModel)
class TestAdmin(DocumentAdmin):
    model = TestModel
