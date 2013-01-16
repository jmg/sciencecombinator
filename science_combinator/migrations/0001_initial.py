# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table('science_combinator_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal('science_combinator', ['Profile'])

        # Adding model 'Entry'
        db.create_table('science_combinator_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['science_combinator.Profile'], null=True)),
            ('votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('submited', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 16, 0, 0))),
        ))
        db.send_create_signal('science_combinator', ['Entry'])

        # Adding M2M table for field voted_by on 'Entry'
        db.create_table('science_combinator_entry_voted_by', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entry', models.ForeignKey(orm['science_combinator.entry'], null=False)),
            ('profile', models.ForeignKey(orm['science_combinator.profile'], null=False))
        ))
        db.create_unique('science_combinator_entry_voted_by', ['entry_id', 'profile_id'])

        # Adding model 'Comment'
        db.create_table('science_combinator_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['science_combinator.Entry'])),
            ('submited', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['science_combinator.Profile'], null=True)),
        ))
        db.send_create_signal('science_combinator', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table('science_combinator_profile')

        # Deleting model 'Entry'
        db.delete_table('science_combinator_entry')

        # Removing M2M table for field voted_by on 'Entry'
        db.delete_table('science_combinator_entry_voted_by')

        # Deleting model 'Comment'
        db.delete_table('science_combinator_comment')


    models = {
        'science_combinator.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['science_combinator.Entry']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'submited': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['science_combinator.Profile']", 'null': 'True'})
        },
        'science_combinator.entry': {
            'Meta': {'object_name': 'Entry'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'submited': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 16, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['science_combinator.Profile']", 'null': 'True'}),
            'voted_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'votes'", 'symmetrical': 'False', 'to': "orm['science_combinator.Profile']"}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'science_combinator.profile': {
            'Meta': {'object_name': 'Profile'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['science_combinator']