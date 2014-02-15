from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from guardian.shortcuts import assign_perm


class Quote(models.Model):
    quote_text = models.TextField()
    quote_source = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, default=1)

    class Meta:
        ordering = ['-added_on']


@receiver(post_save, sender=Quote)
def set_perms(sender, **kwargs):
    if kwargs['created']:
        quote = kwargs['instance']
        assign_perm('change_quote', quote.added_by, quote)
        assign_perm('delete_quote', quote.added_by, quote)
