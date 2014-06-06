from django.conf.urls import include, url, patterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from probe_project import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.home, name="home"),
                       url(r'^dashboard/', include('probe_project.apps.probe_dispatcher.urls')),

                       # Login / register
                       url(r'^register/$', views.custom_register, name='register'),
                       url(r'^login/$', views.custom_login, name='login'),
                       url(r'^logout/$', views.custom_logout, {'next_page': '/'}, name='logout'),

                       # probe file url
                       url(r'^p/(?P<id>\d+)_(?P<hash>[0-9a-fA-F]{40}).js$',
                           'probe_project.apps.probe_dispatcher.views.probe_file',
                           name="probe"),

                       # rest_framework
                       url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),

                       # localeurl (language selection)
                       (r'^localeurl/', include('localeurl.urls')),

                       # django admin
                       url(r'^admin/', include(admin.site.urls)),

                       #userena
                       (r'^accounts/', include('userena.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'media/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT}),
    )

