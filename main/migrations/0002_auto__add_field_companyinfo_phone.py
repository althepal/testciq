# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CompanyInfo.phone'
        db.add_column(u'main_companyinfo', 'phone',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CompanyInfo.phone'
        db.delete_column(u'main_companyinfo', 'phone')


    models = {
        u'main.address': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'main.companyinfo': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'CompanyInfo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['main']