# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SearchTerm'
        db.create_table('science_combinator_searchterm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal('science_combinator', ['SearchTerm'])

        # Adding model 'Config'
        db.create_table('science_combinator_config', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 22, 0, 0))),
        ))
        db.send_create_signal('science_combinator', ['Config'])

        # Adding model 'AcceptedCaterory'
        db.create_table('science_combinator_acceptedcaterory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('science_combinator', ['AcceptedCaterory'])


    def backwards(self, orm):
        # Deleting model 'SearchTerm'
        db.delete_table('science_combinator_searchterm')

        # Deleting model 'Config'
        db.delete_table('science_combinator_config')

        # Deleting model 'AcceptedCaterory'
        db.delete_table('science_combinator_acceptedcaterory')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'science_combinator.acceptedcaterory': {
            'Meta': {'object_name': 'AcceptedCaterory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'science_combinator.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['science_combinator.Entry']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submited': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['science_combinator.Profile']", 'null': 'True'})
        },
        'science_combinator.config': {
            'Meta': {'object_name': 'Config'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 22, 0, 0)'})
        },
        'science_combinator.entry': {
            'Meta': {'object_name': 'Entry'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'submited': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 22, 0, 0)'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['science_combinator.Profile']", 'null': 'True'}),
            'voted_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'votes'", 'symmetrical': 'False', 'to': "orm['science_combinator.Profile']"}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'science_combinator.profile': {
            'Meta': {'object_name': 'Profile', '_ormbases': ['auth.User']},
            'entries': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['science_combinator.Entry']", 'symmetrical': 'False'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'science_combinator.searchterm': {
            'Meta': {'object_name': 'SearchTerm'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['science_combinator']