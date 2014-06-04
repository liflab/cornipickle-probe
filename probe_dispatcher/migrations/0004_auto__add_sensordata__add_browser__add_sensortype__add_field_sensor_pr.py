# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SensorData'
        db.create_table(u'probe_dispatcher_sensordata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['probe_dispatcher.Sensor'])),
            ('browser', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['probe_dispatcher.Browser'])),
            ('data', self.gf('picklefield.fields.PickledObjectField')()),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'probe_dispatcher', ['SensorData'])

        # Adding model 'Browser'
        db.create_table(u'probe_dispatcher_browser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'probe_dispatcher', ['Browser'])

        # Adding model 'SensorType'
        db.create_table(u'probe_dispatcher_sensortype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1200)),
            ('prototype_properties', self.gf('picklefield.fields.PickledObjectField')()),
            ('prototype_data', self.gf('picklefield.fields.PickledObjectField')()),
        ))
        db.send_create_signal(u'probe_dispatcher', ['SensorType'])

        # Removing M2M table for field sensors on 'Probe'
        db.delete_table(db.shorten_name(u'probe_dispatcher_probe_sensors'))

        # Adding field 'Sensor.probe'
        db.add_column(u'probe_dispatcher_sensor', 'probe',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['probe_dispatcher.Probe']),
                      keep_default=False)

        # Adding field 'Sensor.sensor_type'
        db.add_column(u'probe_dispatcher_sensor', 'sensor_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['probe_dispatcher.SensorType']),
                      keep_default=False)

        # Adding field 'Sensor.properties'
        db.add_column(u'probe_dispatcher_sensor', 'properties',
                      self.gf('picklefield.fields.PickledObjectField')(default={}),
                      keep_default=False)

        # Adding field 'Sensor.description'
        db.add_column(u'probe_dispatcher_sensor', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=1200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'SensorData'
        db.delete_table(u'probe_dispatcher_sensordata')

        # Deleting model 'Browser'
        db.delete_table(u'probe_dispatcher_browser')

        # Deleting model 'SensorType'
        db.delete_table(u'probe_dispatcher_sensortype')

        # Adding M2M table for field sensors on 'Probe'
        m2m_table_name = db.shorten_name(u'probe_dispatcher_probe_sensors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('probe', models.ForeignKey(orm[u'probe_dispatcher.probe'], null=False)),
            ('sensor', models.ForeignKey(orm[u'probe_dispatcher.sensor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['probe_id', 'sensor_id'])

        # Deleting field 'Sensor.probe'
        db.delete_column(u'probe_dispatcher_sensor', 'probe_id')

        # Deleting field 'Sensor.sensor_type'
        db.delete_column(u'probe_dispatcher_sensor', 'sensor_type_id')

        # Deleting field 'Sensor.properties'
        db.delete_column(u'probe_dispatcher_sensor', 'properties')

        # Deleting field 'Sensor.description'
        db.delete_column(u'probe_dispatcher_sensor', 'description')


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
        u'probe_dispatcher.browser': {
            'Meta': {'object_name': 'Browser'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'probe_dispatcher.probe': {
            'Meta': {'object_name': 'Probe'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1200'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'probe_dispatcher.sensor': {
            'Meta': {'object_name': 'Sensor'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'probe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['probe_dispatcher.Probe']"}),
            'properties': ('picklefield.fields.PickledObjectField', [], {}),
            'sensor_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['probe_dispatcher.SensorType']"})
        },
        u'probe_dispatcher.sensordata': {
            'Meta': {'object_name': 'SensorData'},
            'browser': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['probe_dispatcher.Browser']"}),
            'data': ('picklefield.fields.PickledObjectField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['probe_dispatcher.Sensor']"})
        },
        u'probe_dispatcher.sensortype': {
            'Meta': {'object_name': 'SensorType'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prototype_data': ('picklefield.fields.PickledObjectField', [], {}),
            'prototype_properties': ('picklefield.fields.PickledObjectField', [], {}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['probe_dispatcher']