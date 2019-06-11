from documents.serializers import DocumentSerializer
from rest_framework import viewsets
from .models import Document
from django.utils import timezone
from django.conf import settings
import os
from django.template.loader import render_to_string
from uuid import uuid4

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        serializer.save(date_create=timezone.now(),
                        user_create=self.request.user,)


def generate_PDF(document, user, template, template_data):

    html_string = render_to_string(template, template_data)
    html = HTML(string=html_string, base_url=settings.BASE_URL)

    css_dir = os.path.join(settings.BASE_DIR, 'static', 'css')

    filename = u'{}.pdf'.format(uuid4())
    path = os.path.join(settings.FILE_DIR, filename)
    f = open(path, "w+b")

    html.write_pdf(f)

    f.close()

    doc_file = Document(
        user = user
    )
    doc_file.doc_file.name = filename
    doc_file.save()

    return document