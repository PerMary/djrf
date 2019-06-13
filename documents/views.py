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

    def pdf_generate(request, id_demand):

        demand = get_object_or_404(Demand, id=id_demand)
        positinons = Position.objects.filter(demand=id_demand)
        user = request.user

        html_string = render_to_string('documents/PDF_for_demand.html',
                                       {'demand':demand,
                                        'positions': positinons})
        html = HTML(string=html_string)
        result = html.write_pdf

        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename=demand.pdf'
        response['Content-Transfer-Encoding'] = 'binary'
        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output = open(output.name, 'r')
            response.write(output.read())


        return response


