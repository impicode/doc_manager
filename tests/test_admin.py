from django.test import TestCase, RequestFactory
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from tests.models import TestModel
from tests.admin import TestAdmin


class FakeUser():
    is_active = True
    is_staff = True
    is_authenticated = True

    def __init__(self):
        pass

    def has_perm(self, str):
        return True


class FakeMessage():
    level = None
    message = None
    extra_tags = None

    def __init__(self):
        pass
    
    def add(self, level, message, extra_tags):
        self.level = level
        self.message = message
        self.extra_tags = extra_tags


class AdminTestClass(TestCase):
    def setUp(self):
        self.site = TestAdmin(model=TestModel, admin_site=AdminSite())
        self.factory = RequestFactory()
    
    def test_get_readonly_fields(self):
        self.assertEqual(self.site.get_readonly_fields(None), ())
        doc = TestModel.objects.create()
        self.assertEqual(
            self.site.get_readonly_fields(None, doc),
            ('add_date', 'pub_date', 'published')
        )

    def test_make_published(self):
        doc1 = TestModel.objects.create()
        doc2 = TestModel.objects.create()
        get_request = self.factory.get('')
        get_request._messages = FakeMessage()
        self.site.make_published(get_request, doc1)
        self.assertTrue(TestModel.objects.get(pk=doc1.pk).published)
        self.site.make_published(get_request, doc2)
        self.assertFalse(TestModel.objects.get(pk=doc1.pk).published)
        self.assertTrue(TestModel.objects.get(pk=doc2.pk).published)

    def test_changeform_view_get(self):
        get_request = self.factory.get('')
        get_request.user = FakeUser()
        val = self.site.changeform_view(get_request)
        self.assertEqual(val.status_code, 200)
