from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from guardian.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import Quote


class AddQuote(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Quote
    fields = ['quote_text', 'quote_source']
    template_name = 'edit.html'
    success_message = "Your quote has been added!"

    def get_context_data(self, **kwargs):
        ctx = super(AddQuote, self).get_context_data(**kwargs)
        ctx['mode'] = 'Add a new'
        return ctx

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(AddQuote, self).form_valid(form)

    def get_success_url(self):
        return reverse('webapp:view_single', args=(self.object.pk,))


class EditQuote(SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'edit.html'
    model = Quote
    fields = ['quote_text', 'quote_source']
    success_message = "Quote has been changed!"
    permission_required = 'auth.change_quote'

    def get_context_data(self, **kwargs):
        ctx = super(EditQuote, self).get_context_data(**kwargs)
        ctx['mode'] = 'Editing'
        ctx['number'] = '#{}'.format(ctx['quote'].pk)
        return ctx

    def get_success_url(self):
        return reverse('webapp:view_single', args=(self.object.pk,))


class ViewQuote(DetailView):
    model = Quote
    template_name = 'quote.html'


class QuoteList(ListView):
    model = Quote
    template_name = 'index.html'
    context_object_name = 'quotes'
    paginate_by = 4


class DeleteQuote(SuccessMessageMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Quote
    success_url = '/'
    success_message = "Quote has been deleted!"
    permission_required = 'auth.delete_quote'
