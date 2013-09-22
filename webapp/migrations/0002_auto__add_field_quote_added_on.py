# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Quote.added_on'
        db.add_column('webapp_quote', 'added_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(1970, 1, 1, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Quote.added_on'
        db.delete_column('webapp_quote', 'added_on')


    models = {
        'webapp.quote': {
            'Meta': {'object_name': 'Quote'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote_source': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quote_text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['webapp']