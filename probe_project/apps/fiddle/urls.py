from django.conf.urls import patterns, url

urlpatterns = patterns('probe_project.apps.fiddle.views',
                       url(r'^fiddleeditor/?$', 'fiddle_editor', name='fiddle_editor'),
)