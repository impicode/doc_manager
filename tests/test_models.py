from django.test import TestCase
from tests.models import TestModel


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
        self.assertFalse(doc1.published)

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
