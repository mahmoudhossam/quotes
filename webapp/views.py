from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from models import *

@require_http_methods(['GET', 'POST'])
def add_quote(request):
    if request.method == 'GET':
        return TemplateResponse(request, 'new.html')
    else:
        text = request.POST.get('quote')
        src = request.POST.get('source')
        quote = Quote(quote_text=text, quote_source=src)
        quote.save()
