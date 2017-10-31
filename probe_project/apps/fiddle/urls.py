from django.conf.urls import patterns, url

urlpatterns = patterns('probe_project.apps.fiddle.views',
                       url(r'^fiddlejs/?$', 'fiddle_js', name='fiddle_js'),
                       url(r'^fiddleeditor/?$', 'fiddle_editor', name='fiddle_editor'),
                       url(r'^getgrammar/?$', 'get_grammar', name='get_grammar'),
)