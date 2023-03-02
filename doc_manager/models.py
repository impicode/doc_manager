# *
# * (c) ImpiCode Sp. z o.o.
# * Stamp: MAL 02.06.2021
# *

import os

from datetime import date
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import gettext_lazy as _


class ContentTypeRestrictedFileField(FileField):
    def __init__(self, content_types=['application/pdf'],
                 max_upload_size=None, upload_to=None, **kwargs):
        self.content_types = content_types
        self.max_upload_size = (
            max_upload_size
            if max_upload_size
            else getattr(settings, 'MAX_FILE_UPLOAD_SIZE', 5242880)
        )
        kwargs['validators'] = [FileExtensionValidator(['pdf'])]
        super(ContentTypeRestrictedFileField, self).__init__(**kwargs)
        self.upload_to = (
            upload_to
            if upload_to
            else getattr(settings, 'FILE_UPLOAD_TO', 'documents/%Y/%m/%d/')
        )

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField,
                     self).clean(*args, **kwargs)

        file = data.file

        if file.content_type not in self.content_types:
            raise forms.ValidationError(_('Filetype not supported.'))

        if file.size > self.max_upload_size:
            raise forms.ValidationError(
                _('Please keep filesize under %s. Current filesize %s')
                % (
                    filesizeformat(self.max_upload_size),
                    filesizeformat(file.size),
                )
            )

        return data


class DocumentManager(models.Manager):
    def published_pdf(self):
        return self.model.objects.filter(published=True).first()

    def set_published(self, pk):
        obj = self.model.objects.get(pk=pk)
        self.model.objects.filter(published=True).update(published=False)
        obj.publish()


class DocumentModel(models.Model):
    add_date = models.DateField(auto_now_add=True, verbose_name=_('Add date'))
    pub_date = models.DateField(null=True, blank=True, verbose_name=_('Publication date'))
    published = models.BooleanField(default=False, verbose_name=_('Published'))
    pdf_file = ContentTypeRestrictedFileField(
                    upload_to='documents/%Y/%m/%d/',
                    verbose_name=_('PDF file')
                )
    objects = DocumentManager()

    class Meta:
        abstract = True
        ordering = ['pub_date']

    def publish(self):
        self.published = True
        self.pub_date = date.today()
        self.save()

    def pdf_filename(self):
        return os.path.basename(self.pdf_file.name)
