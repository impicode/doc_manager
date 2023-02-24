from django.test import TestCase
from tests.models import TestModel
from doc_manager.models import ContentTypeRestrictedFileField
from django.core.exceptions import ValidationError


class TestFile():
    content_type = ''
    size = 0

    def __init__(self, content_type, size):
        self.content_type = content_type
        self.size = size


class TestValue():
    file = None
    name = ''
    content_type = ''

    def __init__(self, name, content_type, size):
        self.file = TestFile(content_type, size)
        self.name = name
        self.content_type = content_type


class DocumentModelTestClass(TestCase):
    def test_published(self):
        doc = TestModel.objects.create()
        TestModel.objects.set_published(doc.pk)
        doc = TestModel.objects.get(pk=doc.pk)
        self.assertTrue(doc.published)

    def test_published_2_docs(self):
        doc1 = TestModel.objects.create()
        doc2 = TestModel.objects.create()
        TestModel.objects.set_published(doc1.pk)
        TestModel.objects.set_published(doc2.pk)
        doc1 = TestModel.objects.get(pk=doc1.pk)
        published_doc = TestModel.objects.published_pdf()
        self.assertFalse(doc1.published)
        self.assertTrue(published_doc.pk == doc2.pk)

    def test_publish_date(self):
        doc = TestModel.objects.create()
        TestModel.objects.set_published(doc.pk)
        doc = TestModel.objects.get(pk=doc.pk)
        self.assertTrue(doc.pub_date)

    def test_published_10_docs(self):
        docs = []
        for i in range(0, 10):
            docs.append(TestModel.objects.create())

        for doc in docs:
            TestModel.objects.set_published(doc.pk)

        for i in range(0, 9):
            self.assertFalse(TestModel.objects.get(pk=docs[i].pk).published)

        self.assertTrue(TestModel.objects.get(pk=docs[9].pk).published)

    def test_wrong_file_extension(self):
        f = ContentTypeRestrictedFileField(upload_to='documents/%Y/%m/%d/')
        try:
            f.clean(value=TestValue('test.txt', 'txt', 10), model_instance='')
            self.fail()
        except ValidationError:
            pass

    def test_correct_file_extension(self):
        f = ContentTypeRestrictedFileField(upload_to='documents/%Y/%m/%d/')
        try:
            f.clean(
                value=TestValue('test.pdf', 'application/pdf', 10),
                model_instance=''
            )
        except ValidationError:
            self.fail()

    def test_to_big_size(self):
        f = ContentTypeRestrictedFileField(
            upload_to='documents/%Y/%m/%d/',
            max_upload_size=10
        )
        try:
            f.clean(
                value=TestValue('test.pdf', 'application/pdf', 100),
                model_instance=''
            )
            self.fail()
        except ValidationError:
            pass
