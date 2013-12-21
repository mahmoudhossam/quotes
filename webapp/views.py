from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Quote


class AddQuote(SuccessMessageMixin, CreateView):
    success_url = '/'
    model = Quote
    fields = ['quote_text', 'quote_source']
    template_name = 'edit.html'
    success_message = "Your quote has been added!"

    def get_context_data(self, **kwargs):
        ctx = super(AddQuote, self).get_context_data(**kwargs)
        ctx['mode'] = 'Add a new'
        return ctx

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddQuote, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(AddQuote, self).form_valid(form)


class EditQuote(SuccessMessageMixin, UpdateView):
    template_name = 'edit.html'
    model = Quote
    success_url = '/'
    fields = ['quote_text', 'quote_source']
    success_message = "Quote has been changed!"

    def get_context_data(self, **kwargs):
        ctx = super(EditQuote, self).get_context_data(**kwargs)
        ctx['mode'] = 'Editing'
        ctx['number'] = '#{}'.format(ctx['quote'].pk)
        return ctx

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditQuote, self).dispatch(*args, **kwargs)


class ViewQuote(DetailView):
    model = Quote
    template_name = 'quote.html'


class QuoteList(ListView):
    model = Quote
    template_name = 'index.html'
    context_object_name = 'quotes'
    paginate_by = 4


class DeleteQuote(SuccessMessageMixin, DeleteView):
    model = Quote
    success_url = '/'
    success_message = "Quote has been deleted!"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteQuote, self).dispatch(*args, **kwargs)
