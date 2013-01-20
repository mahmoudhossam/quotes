from django.db import models

# Create your models here.

class Quote(models.Model):
    quote_text = models.TextField()
    quote_source = models.CharField(max_length=100)
