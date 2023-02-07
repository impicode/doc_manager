from django.views import View
from django.http import Http404, FileResponse


class DocumentView(View):
    model = None

    def get(self, request):
        file_obj = self.model.objects.published_pdf()
        if file_obj is None:
            raise Http404
        pdf_file = file_obj.pdf_file
        if pdf_file is None:
            raise Http404
        response = FileResponse(pdf_file, as_attachment=False,
                                content_type="application/pdf")
        return response
