from django.conf.urls import patterns, url

url_patterns = patterns('probe_project.apps.probe_parser.views',
                       url(r'^parser/$', 'parser', name="parser"),
)