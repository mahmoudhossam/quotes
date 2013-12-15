from django.db import models
from django.contrib.auth.models import User


class Quote(models.Model):
    quote_text = models.TextField()
    quote_source = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, default=1)

    class Meta:
        ordering = ['-added_on']
