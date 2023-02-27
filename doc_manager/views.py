from django.views import View
from django.http import Http404, FileResponse


class DocumentView(View):
    model = None

    def get(self, request):
        document_model = self.model.objects.published()
        if document_model is None:
            raise Http404
        file = document_model.file_obj
        if file is None:
            raise Http404
        filename = document_model.filename()
        if filename.endswith('.html'):
            response = FileResponse(file, as_attachment=False,
                                    content_type='text/html')
        elif filename.endswith('.pdf'):
            response = FileResponse(file, as_attachment=False,
                                    content_type='application/pdf')
        return response
