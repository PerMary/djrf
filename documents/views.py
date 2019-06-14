from documents.serializers import DocumentSerializer
from weasyprint import HTML
from rest_framework import viewsets
from .models import Document
from django.utils import timezone
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from demands.models import Demand,Position
import tempfile

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        serializer.save(date_create=timezone.now(),
                        user_create=self.request.user,)


