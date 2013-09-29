from django import forms
from .models import Quote


class AddForm(forms.ModelForm):
    class Meta:
        model = Quote
        exclude = ('added_on', 'added_by')
