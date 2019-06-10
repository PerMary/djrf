from django.shortcuts import render
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from core import settings

HTML('http://samplewebsite.com/').write_pdf('/localdirectory/test.pdf',

        stylesheets=[CSS(string='body { font-size: 10px }')])