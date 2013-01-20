# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quote'
        db.create_table('webapp_quote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote_text', self.gf('django.db.models.fields.TextField')()),
            ('quote_source', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('webapp', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table('webapp_quote')


    models = {
        'webapp.quote': {
            'Meta': {'object_name': 'Quote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote_source': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote_text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['webapp']