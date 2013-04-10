# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'SiteUser', fields ['username']
        db.delete_unique(u'accounts_siteuser', ['username'])

        # Deleting field 'SiteUser.is_staff'
        db.delete_column(u'accounts_siteuser', 'is_staff')

        # Deleting field 'SiteUser.date_joined'
        db.delete_column(u'accounts_siteuser', 'date_joined')

        # Deleting field 'SiteUser.is_superuser'
        db.delete_column(u'accounts_siteuser', 'is_superuser')

        # Adding field 'SiteUser.is_admin'
        db.add_column(u'accounts_siteuser', 'is_admin',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Removing M2M table for field groups on 'SiteUser'
        db.delete_table('accounts_siteuser_groups')

        # Removing M2M table for field user_permissions on 'SiteUser'
        db.delete_table('accounts_siteuser_user_permissions')


        # Changing field 'SiteUser.username'
        db.alter_column(u'accounts_siteuser', 'username', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'SiteUser.first_name'
        db.alter_column(u'accounts_siteuser', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'SiteUser.last_name'
        db.alter_column(u'accounts_siteuser', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'SiteUser.email'
        db.alter_column(u'accounts_siteuser', 'email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=255))
        # Adding index on 'SiteUser', fields ['email']
        db.create_index(u'accounts_siteuser', ['email'])

        # Adding unique constraint on 'SiteUser', fields ['email']
        db.create_unique(u'accounts_siteuser', ['email'])


    def backwards(self, orm):
        # Removing unique constraint on 'SiteUser', fields ['email']
        db.delete_unique(u'accounts_siteuser', ['email'])

        # Removing index on 'SiteUser', fields ['email']
        db.delete_index(u'accounts_siteuser', ['email'])

        # Adding field 'SiteUser.is_staff'
        db.add_column(u'accounts_siteuser', 'is_staff',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'SiteUser.date_joined'
        db.add_column(u'accounts_siteuser', 'date_joined',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'SiteUser.is_superuser'
        db.add_column(u'accounts_siteuser', 'is_superuser',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'SiteUser.is_admin'
        db.delete_column(u'accounts_siteuser', 'is_admin')

        # Adding M2M table for field groups on 'SiteUser'
        db.create_table(u'accounts_siteuser_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('siteuser', models.ForeignKey(orm[u'accounts.siteuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(u'accounts_siteuser_groups', ['siteuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'SiteUser'
        db.create_table(u'accounts_siteuser_user_permissions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('siteuser', models.ForeignKey(orm[u'accounts.siteuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(u'accounts_siteuser_user_permissions', ['siteuser_id', 'permission_id'])


        # Changing field 'SiteUser.username'
        db.alter_column(u'accounts_siteuser', 'username', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True))
        # Adding unique constraint on 'SiteUser', fields ['username']
        db.create_unique(u'accounts_siteuser', ['username'])


        # Changing field 'SiteUser.first_name'
        db.alter_column(u'accounts_siteuser', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'SiteUser.last_name'
        db.alter_column(u'accounts_siteuser', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'SiteUser.email'
        db.alter_column(u'accounts_siteuser', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75))

    models = {
        u'accounts.siteuser': {
            'Meta': {'object_name': 'SiteUser'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['accounts']