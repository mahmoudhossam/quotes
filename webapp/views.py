from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import AddForm
from .models import Quote


class AddQuote(CreateView):
    success_url = '/'
    form_class = AddForm
    template_name = 'edit.html'

    def get_context_data(self, **kwargs):
        ctx = super(AddQuote, self).get_context_data(**kwargs)
        ctx['mode'] = 'Adding new'
        return ctx


class EditQuote(UpdateView):
    template_name = 'edit.html'
    model = Quote
    success_url = '/'
    fields = ['quote_text', 'quote_source']

    def get_context_data(self, **kwargs):
        ctx = super(EditQuote, self).get_context_data(**kwargs)
        ctx['mode'] = 'Editing'
        ctx['number'] = '#{}'.format(ctx['quote'].pk)
        return ctx


class ViewQuote(DetailView):
    model = Quote
    template_name = 'quote.html'


class QuoteList(ListView):
    model = Quote
    template_name = 'index.html'
    context_object_name = 'quotes'


class DeleteQuote(DeleteView):
    model = Quote
    template_name = 'delete.html'
    success_url = '/'
