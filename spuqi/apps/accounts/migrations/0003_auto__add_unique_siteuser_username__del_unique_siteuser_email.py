# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'SiteUser', fields ['email']
        db.delete_unique(u'accounts_siteuser', ['email'])

        # Adding index on 'SiteUser', fields ['username']
        db.create_index(u'accounts_siteuser', ['username'])

        # Adding unique constraint on 'SiteUser', fields ['username']
        db.create_unique(u'accounts_siteuser', ['username'])

        # Removing index on 'SiteUser', fields ['email']
        db.delete_index(u'accounts_siteuser', ['email'])


    def backwards(self, orm):
        # Adding index on 'SiteUser', fields ['email']
        db.create_index(u'accounts_siteuser', ['email'])

        # Removing unique constraint on 'SiteUser', fields ['username']
        db.delete_unique(u'accounts_siteuser', ['username'])

        # Removing index on 'SiteUser', fields ['username']
        db.delete_index(u'accounts_siteuser', ['username'])

        # Adding unique constraint on 'SiteUser', fields ['email']
        db.create_unique(u'accounts_siteuser', ['email'])


    models = {
        u'accounts.siteuser': {
            'Meta': {'object_name': 'SiteUser'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['accounts']