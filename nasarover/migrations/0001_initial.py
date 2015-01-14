# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Grid'
        db.create_table(u'nasarover_grid', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('x_len', self.gf('django.db.models.fields.IntegerField')()),
            ('y_len', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'nasarover', ['Grid'])

        # Adding model 'Mineral'
        db.create_table(u'nasarover_mineral', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'nasarover', ['Mineral'])

        # Adding model 'SubGrid'
        db.create_table(u'nasarover_subgrid', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('g_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nasarover.Grid'])),
            ('pos_x', self.gf('django.db.models.fields.IntegerField')()),
            ('pos_y', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'nasarover', ['SubGrid'])

        # Adding model 'MineralDis'
        db.create_table(u'nasarover_mineraldis', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sg_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nasarover.SubGrid'])),
            ('mi_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nasarover.Mineral'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'nasarover', ['MineralDis'])

        # Adding model 'Rover'
        db.create_table(u'nasarover_rover', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('sg_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nasarover.SubGrid'])),
            ('dirn', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'nasarover', ['Rover'])

        # Adding model 'RoverSen'
        db.create_table(u'nasarover_roversen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('r_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nasarover.Rover'])),
            ('m_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nasarover.Mineral'])),
        ))
        db.send_create_signal(u'nasarover', ['RoverSen'])

        # Adding unique constraint on 'RoverSen', fields ['r_id', 'm_id']
        db.create_unique(u'nasarover_roversen', ['r_id_id', 'm_id_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'RoverSen', fields ['r_id', 'm_id']
        db.delete_unique(u'nasarover_roversen', ['r_id_id', 'm_id_id'])

        # Deleting model 'Grid'
        db.delete_table(u'nasarover_grid')

        # Deleting model 'Mineral'
        db.delete_table(u'nasarover_mineral')

        # Deleting model 'SubGrid'
        db.delete_table(u'nasarover_subgrid')

        # Deleting model 'MineralDis'
        db.delete_table(u'nasarover_mineraldis')

        # Deleting model 'Rover'
        db.delete_table(u'nasarover_rover')

        # Deleting model 'RoverSen'
        db.delete_table(u'nasarover_roversen')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'nasarover.grid': {
            'Meta': {'object_name': 'Grid'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'x_len': ('django.db.models.fields.IntegerField', [], {}),
            'y_len': ('django.db.models.fields.IntegerField', [], {})
        },
        u'nasarover.mineral': {
            'Meta': {'object_name': 'Mineral'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'nasarover.mineraldis': {
            'Meta': {'object_name': 'MineralDis'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mi_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nasarover.Mineral']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'sg_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nasarover.SubGrid']"})
        },
        u'nasarover.rover': {
            'Meta': {'object_name': 'Rover'},
            'dirn': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sg_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nasarover.SubGrid']"}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'nasarover.roversen': {
            'Meta': {'unique_together': "(('r_id', 'm_id'),)", 'object_name': 'RoverSen'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nasarover.Mineral']"}),
            'r_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nasarover.Rover']"})
        },
        u'nasarover.subgrid': {
            'Meta': {'object_name': 'SubGrid'},
            'g_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nasarover.Grid']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pos_x': ('django.db.models.fields.IntegerField', [], {}),
            'pos_y': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['nasarover']