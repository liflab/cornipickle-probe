from django.conf.urls import patterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls import include, url
from probe_project import views as probe_views
from custom_userena_urls import urlpatterns as custom_userena_urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', probe_views.home, name="home"),
    url(r'^manager/', include('probe_project.apps.probe_dispatcher.urls')),
    url(r'^dashboards/', include('probe_project.apps.dashboards.urls')),
    url(r'^fiddle/', include('probe_project.apps.fiddle.urls')),

    url(r'^image/$', 'probe_project.apps.dashboards.views.image', name='image'),

    url(r'^preevaluate/$', 'probe_project.apps.dashboards.views.image', name='preevaluate'),

    # probe file url
    url(r'^p/(?P<probe_id>\d+)_(?P<probe_hash>[0-9a-fA-F]{40}).js$',
        'probe_project.apps.probe_dispatcher.views.probe_file',
        name="probe"),

    # probe file test url
    url(r'^p/(?P<probe_id>\d+)_(?P<probe_hash>[0-9a-fA-F]{40}).html$',
        'probe_project.apps.probe_dispatcher.views.probe_test',
        name="probe_test"),

    # rest_framework
    url(r'^api/?', include('rest_framework.urls', namespace='rest_framework')),

    # localeurl (language selection)
    (r'^localeurl/', include('localeurl.urls')),

    # django admin
    url(r'^admin/', include(admin.site.urls), name='administration'),

    # userena
    url(r'^', include(custom_userena_urls)),

    # Social Auth
    url(r'social/', include('social.apps.django_app.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'uploads/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )