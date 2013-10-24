# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.author'
        db.delete_column(u'microblogs_post', 'author_id')


    def backwards(self, orm):
        # Adding field 'Post.author'
        db.add_column(u'microblogs_post', 'author',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='posts', to=orm['auth.User']),
                      keep_default=False)


    models = {
        u'microblogs.post': {
            'Meta': {'ordering': "['-created_at', 'title']", 'object_name': 'Post'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['microblogs']