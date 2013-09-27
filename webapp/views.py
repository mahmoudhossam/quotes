from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import AddForm
from .models import Quote


class AddQuote(CreateView):
    template_name = 'new.html'
    form_class = AddForm
    success_url = '/'


class QuoteList(ListView):
    model = Quote
    template_name = 'index.html'
    context_object_name = 'quotes'
